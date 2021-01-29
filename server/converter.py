"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
# coding: utf-8
import asyncio
import logging
import re
import tempfile
from pathlib import Path
from typing import List, Iterator
from google.cloud import texttospeech
from google.oauth2 import service_account


logger = logging.getLogger(__name__)


class GoogleTTS(object):
    def __init__(self, text: str):
        self.text = text
        self.credentials = service_account.Credentials.from_service_account_file("google-tts-key.json")

    async def save(self, file_path: str) -> bool:
        # Instantiates a client
        async_client = texttospeech.TextToSpeechAsyncClient(credentials=self.credentials)

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=self.text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            # default
            # language_code="zh-CN", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            # wavenet
            language_code="cmn-CN",
            name="cmn-CN-Wavenet-A",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = await async_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

        # The response's audio_content is binary.
        with open(file_path, "wb") as out:
            out.write(response.audio_content)
            print(f"Audio content written to file {file_path}")
        return True


MAX_CHARS = 500

# API supports max 5000 chars per request.
def segments(sents: List[str], maxchars: int = MAX_CHARS) -> Iterator:
    i = 0
    while True:
        curseg = []
        count = 0
        while i < len(sents):
            sent = sents[i]
            if len(curseg) > 0 and count + 5 + len(sent) >= maxchars:
                break
            curseg.append(sent)
            count += 5 + len(sent)
            i += 1
        if len(curseg) > 0:
            # Sentences better be split with ". " or ".\n" - if you split with two spaces ".  "
            # then the API doesn't pause for very long in between sentences, for some reason!
            yield ".\n".join(curseg)
        else:
            break


def make_segments(text: str) -> List[str]:
    newlines = re.compile(r"\n+")
    # 先按自然段分
    sents = [par for par in newlines.split(text.strip()) if par]
    segs = []
    for sent in sents:
        # 超过最大支持长度，按自然语句划分
        if len(sent) >= MAX_CHARS:
            parts = list(segments(re.split(r"(？|。|」|！)+", sent.strip(), flags=re.MULTILINE)))
            segs.extend(parts)
        else:
            segs.append(sent)
    # 减少段落数目
    segs = list(segments(segs))
    return segs


def make_audios(segs: List[str], folder: str):

    media_dir = Path(folder)

    logger.info("spooling %s sentences to temp dir %s", len(segs), media_dir)

    async def main():
        tasks = []
        for i, seg in enumerate(segs):
            tts = GoogleTTS(seg)
            # tts.save(media_dir / f"{i}.mp3")
            tasks.append(tts.save(media_dir / f"{i}.mp3"))
        print(len(tasks))
        await asyncio.gather(*tasks)

    asyncio.run(main())


if __name__ == "__main__":
    with open("text.txt") as f:
        segs = make_segments(f.read())
        make_audios(segs, tempfile.mkdtemp("podcastx"))

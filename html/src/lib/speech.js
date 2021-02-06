function getWordsCount(v) {
    const matches = v.match(/\S+/g);
    return matches ? matches.length : 0;
}

export class Speech {
    /**
     * Speech constructor. Converts text into chunks, then tries to read them.
     * @param text
     */
    constructor({
                    chunks, _id, title, author, favicon,
                    speaker = 'male', auth_token = '',
                    id, image, url, domain, pinned, progress = 0
                }) {
        this.title = title;
        this.author = author;
        this.favicon = favicon || image;
        this._speaker = speaker;
        this.id = id || _id.$oid;

        this.chunks = chunks.map(i => ({text: i, audio: new Audio()}));
        this.length = this.chunks.length;
        this.index = 0;
        this._playingState = 'idle';

        this._audio = new Audio();
        this._volume = 0.8;

        this._word_count = getWordsCount(this.chunks.map(i => i.text).join(' '));
        this.url = url;
        this.domain = domain;
        this.auth_token = auth_token;
        this.pinned = pinned;

        this.progress = progress;
    }

    /**
     * Load audio for chunk
     * @param chunk
     * @private
     */
    _loadAudio(index) {
        const chunk = this.chunks[index];
        console.log(`loading chunk ${chunk.text}`);
        if (!chunk.audio.src) {
            chunk.audio.src = `${Speech.API_URL}/api/article_podcast/listen?podcastId=${this.id}&chunk=${index}&gender=${this.speaker}&token=${this.auth_token}&_t=${Math.random()}.mp3`;
        }
    }

    /**
     * Play chunk by index. tries to load the chunk, then plays it
     * Also sets callback to play next chunk if there exists one.
     * @param index
     * @private
     */
    _playByIndex(index = 0) {
        if (index === this.length) {
            this.stop();
            this.onended && this.onended(this);
            return;
        }

        const playbackRate = this._audio.playbackRate;
        const currentChunk = this.chunks[index];
        this._loadAudio(index);
        if (index !== this.length - 1) {
            this._loadAudio(index + 1);
        }

        this._audio.src = currentChunk.audio.src;
        this._audio.play();
        this._audio.playbackRate = playbackRate;
        this._audio.onended = () => {
            this._playByIndex(index + 1)
        };

        this.index = index;
    }

    _cleanCache() {
        for (let chunk of this.chunks) {
            chunk.audio = new Audio();
        }
    }

    onended() {
        console.log('ended');
    }

    /**
     * Play the speech. Starts from current index
     */
    play() {
        if (this._playingState === 'play') {
            return;
        }

        this._playByIndex(this.index);
        this._playingState = 'play';
    }

    /**
     * Stop the speech.
     * Pauses the current speech and sets the index to 0.
     */
    stop() {
        this.pause();
        this._playingState = 'idle';
        this.index = 0;
    }

    /**
     * Pause the speech.
     * Just pauses current playing audio.
     */
    pause() {
        this._audio.pause();
        this._playingState = 'idle';
    }

    /**
     * Toggle the speech.
     * Pause if playing. Play if not playing
     */
    toggle() {
        if (this._playingState === 'idle') {
            this.play();
        } else {
            this.pause();
        }
    }

    /**
     * Get current state
     * @returns {{volume: number, playingState: string, playbackRate: number, total: *, favicon: *, author: *, index: number, title: *}}
     */
    get state() {
        return {
            title: this.title,
            author: this.author,
            favicon: this.favicon,
            index: this.index,
            total: this.chunks.length,
            volume: this._volume,
            playingState: this._playingState,
            playbackRate: this.playbackRate,
            gender: this._speaker,
            id: this.id,
            duration: this.duration,
            secondsPlayed: this.secondsPlayed,
            url: this.url,
            domain: this.domain

        }
    }

    get duration() {
        return Math.round(this._word_count / 2.5);
    }

    get secondsPlayed() {
        const playedSentences = getWordsCount(this.chunks.slice(0, this.index).map(i => i.text).join(' '));
        return Math.round(playedSentences / 2.5 + this._audio.currentTime);
    }

    get progress() {
        return Math.round(this.index / this.chunks.length * 100);
    }

    set progress(p) {
        let continueAfterSet = false;
        if (this._playingState === 'play') {
            this.pause();
            continueAfterSet = true;
        }
        this.index = Math.floor(this.chunks.length * p);
        if (continueAfterSet) {
            this.play();
        }
    }

    set volume(v) {
        this._volume = v;
        this._audio.volume = v;
    }

    get playbackRate() {
        return this._audio.playbackRate
    }

    set playbackRate(v) {
        this._audio.playbackRate = v
    }

    get speaker() {
        return this._speaker;
    }

    set speaker(v) {
        if (this._speaker === v) {
            return;
        }

        let continueAfterSet = this._playingState === 'play';
        this.pause();
        this._cleanCache();
        this._speaker = v;
        if (continueAfterSet) {
            this.play();
        }
    }
}

Speech.API_URL = '';
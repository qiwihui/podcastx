db.createUser({
    user: "mongo",
    pwd: "mongo-password",
    roles: [
        {
            role: "readWrite",
            db: "podcastx"
        }
    ]
})
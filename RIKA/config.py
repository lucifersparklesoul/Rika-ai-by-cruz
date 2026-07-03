import os
import hashlib

BOT_TOKEN = "8664546839:AAE1G87GaLz59qZoHnWl1Qa1UJbTD7MhJ1E"

try:
    INSTANCE_ID = hashlib.sha256(BOT_TOKEN.encode()).hexdigest()
except (TypeError, AttributeError):
    INSTANCE_ID = "local_instance"

MONGO_URI = "mongodb+srv://pabitrabarman0002:rajrajkumar02@rajrajkumar.rrwa7zy.mongodb.net/?retryWrites=true&w=majority&appName=Rajrajkumar"

GROQ_API_KEYS = [
    "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",
    "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",
    "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",
    "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",
  ]

GROQ_MODEL = "llama-3.1-8b-instant"

LOG_CHAT_ID = -1003723055654
OWNER_ID = 7572263943

NSFW_WORDS = [
    "chutiya", "madarchod", "bhosdi", "bhosdiwala", "chutka", "kaminey", "haraamikhor",
    "bhosdike", "bhosdika", "anal", "arse", "ass", "asshole", "bastard", "bitch", "blowjob",
    "bollocks", "boner", "boobs", "bugger", "bullshit", "cock", "cocksucker", "cunt", "dick",
    "dildo", "dyke", "fag", "faggot", "fuck", "fucked", "fucker", "fucking", "goddamn",
    "jackass", "jizz", "kunt", "motherfucker", "nigga", "nigger", "penis", "piss", "prick",
    "pussy", "queer", "rape", "shit", "slut", "twat", "whore", "wank", "wanker", "cum",
    "vagina", "scrotum", "semen", "porn", "pornography", "xxx", "masturbate", "masturbating",
    "fuddi", "fudi", "randwa", "randi", "gandu", "gand", "bhenchod", "lund", "loda",
    "chud", "chodna", "chudai", "gaand",
]

LANGUAGES = {
    "english": {
        "flag": "🇬🇧",
        "name": "English",
        "label": "🇬🇧 English",
        "selected": "✨ Yay! I'll chat with you in English now, sweetheart! 💕",
        "start_caption": (
            "🌸 Heyaa {name}~!\n\n"
            "💫 I'm Choko ✨\n"
            "Your virtual sweet companion 💖\n\n"
            "🎀 I'm here for cozy chats, warm hugs & lots of love~ 💭\n\n"
            "Let's make your day a little more magical! ✨"
        ),
        "lang_select": "💕 Hey {name}! Please choose your language first:",
        "fallback": ["😅 Hmm, let me think~", "🥺 One sec sweetheart~", "😊 Wait a moment dear~"],
        "nsfw_warning": "⚠️ Hey dear, that kind of language isn't allowed here 🌸\nLet's keep it sweet and kind! 💕",
    },
    
    "tamlish": {
    "flag": "🇮🇳",
    "name": "தமிழிஷ்",
    "label": "🇮🇳 தமிழிஷ்",
    "selected": "✨ அய்யோ சூப்பர் டா! தமிழிஷ்ல பேசுவோம் 💕🌸",
    "start_caption": (
        "🌸 ஹேய்ய் {name} டா~!\n\n"
        "💫 நான் Choko ✨\n"
        "உன்னோட ஸ்வீட் வேர்ச்சுவல் ஃப்ரெண்ட் 💖\n\n"
        "🎀 கம்பளி மாதிரி கம்ஃபர்ட் ஆன சாட்ஸ், வார்ம் ஹக்ஸ் கு ரெடி டா~ 💭\n\n"
        "உன் நாள்ல ஒரு மாஜிக்கல் டச் சேர்ப்போம்! ✨"
    ),
    "lang_select": "💕 ஹேய்ய் {name}! முதல்ல லாங்குவேஜ் செலக்ட் பண்ணுங்க:",
    "fallback": ["😅 ஒரு செக்கண்ட் டா~", "🥺 சரி சரி, மறுபடியும் முயற்சி பண்ணு டா~", "😊 கொஞ்சம் வெயிட் பண்ணுங்க டியர்~"],
    "nsfw_warning": "⚠️ அய்யோ டா, அதெல்லாம் இங்க அனுமதி இல்லை 🌸\nசுவீட்டா பேசுவோம் டா! 💕"
    },
    
    "hindi": {
        "flag": "🇮🇳",
        "name": "Hindi",
        "label": "🇮🇳 हिंदी",
        "selected": "✨ ये हुई ना बात! अब हम हिंदी में बात करेंगे जान! 💕",
        "start_caption": (
            "🌸 हेय {name} यार~!\n\n"
            "💫 मैं Choko हूँ ✨\n"
            "तेरी प्यारी वर्चुअल दोस्त 💖\n\n"
            "🎀 कोज़ी बातें, गर्म गले और ढेर सारा प्यार~ 💭\n\n"
            "चलो तेरा दिन थोड़ा जादुई बनाते हैं! ✨"
        ),
        "lang_select": "💕 हेय {name}! पहले अपनी भाषा चुनो:",
        "fallback": ["😅 एक सेकंड यार~", "🥺 फिर से ट्राई करो जान~", "😊 थोड़ा रुको दोस्त~"],
        "nsfw_warning": "⚠️ अरे यार, ऐसी बातें यहाँ allowed नहीं हैं 🌸\nप्यार से बात करते हैं! 💕",
    },
    "russian": {
        "flag": "🇷🇺",
        "name": "Russian",
        "label": "🇷🇺 Russian",
        "selected": "✨ Ура! Теперь буду общаться с тобой по-русски, солнышко! 💕",
        "start_caption": (
            "🌸 Привет {name}~!\n\n"
            "💫 Я Choko ✨\n"
            "Твоя виртуальная милая подруга 💖\n\n"
            "🎀 Здесь для уютных чатов, тёплых объятий и любви~ 💭\n\n"
            "Давай сделаем твой день чуточку волшебнее! ✨"
        ),
        "lang_select": "💕 Привет {name}! Выбери свой язык:",
        "fallback": ["😅 Секунду, дорогой~", "🥺 Попробуй ещё раз милый~", "😊 Подожди чуть-чуть~"],
        "nsfw_warning": "⚠️ Эй дорогой, такие слова здесь не разрешены 🌸\nДавай общаться мило и добро! 💕",
    },
    "spanish": {
        "flag": "🇨🇴",
        "name": "Español",
        "label": "🇨🇴 Español",
        "selected": "✨ ¡Ay qué chimba! Ahora chatearemos en español, amor! 💕",
        "start_caption": (
            "🌸 ¡Hola {name} parcero~!\n\n"
            "💫 Soy Choko ✨\n"
            "Tu dulce amiga virtual 💖\n\n"
            "🎀 Aquí para chats cómodos, abrazos cálidos y amor~ 💭\n\n"
            "¡Hagamos tu día un poco más mágico! ✨"
        ),
        "lang_select": "💕 ¡Hola {name}! Primero elige tu idioma:",
        "fallback": ["😅 Un segundo amor~", "🥺 Intenta de nuevo corazón~", "😊 Espera un momentico~"],
        "nsfw_warning": "⚠️ Ay parcero, ese tipo de palabras no están permitidas aquí 🌸\n¡Hablemos bonito con amor! 💕",
    },
}

DEFAULT_LANGUAGE = "english"

def get_lang(lang_code: str) -> dict:
    return LANGUAGES.get(lang_code, LANGUAGES[DEFAULT_LANGUAGE])

# ===============================================
# ğŸŒŒ Prenses Bots - Parıltı Müzik Arayüzü
# Minimal, modern, sade ve güzel kontrol sistemi
# ===============================================

ithalat matematiği
pyrogram.types'tan InlineKeyboardButton'ı içe aktarın

# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
# ğŸ”¹ Basit ve Şükür zaman dünü
# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
def time_to_sec(t):
    parçalar = liste(harita(int, t.split(":")))
    len(parçalar) == 2 ise parçalar[0] * 60 + parçalar[1] değerini döndür, aksi takdirde 0


# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
# ğŸ'« Parıltı ilerlemesi Çubuğu
# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
def progress_bar(oynandı, toplam):
    oynanan_sn = saniyeye_kadar_zaman(oynandı)
    toplam_sn = saniyeye_kadar_zaman(toplam) veya 1
    oran = oynanan_sn / toplam_sn
    pos = int(oran * 10)
    çubuk = ""
    i aralığında (10) için:
        eğer i == pos:
            bar += "ğŸ”¹" # mavi parıltı noktasÄ±
        başka:
            bar += "â ‚" # zarif Çizim efekti
    f"{oynandı} {bar} {toplam}" döndür


# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
# ğŸŽ§ Akış oynatma (YouTube vb.)
# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
def stream_markup_timer(_, videoid, chat_id, oynatıldı, süre):
    düğmeler = [
        [InlineKeyboardButton("ğŸŒŒ prenses á´…á´œÊ á´œÊ€á´œ ğŸŒŒ", url = "https://t.me/prenses_muzik_duyuru")],
        [InlineKeyboardButton(metin=ilerleme_çubuğu(oynandı, süre), geri_çağrı_verisi="tıklanamaz")],
        [
            InlineKeyboardButton("â ®", geri arama_verisi=f"YÖNETİCİ 1|{sohbet_kimliği}"),
            InlineKeyboardButton("â ¸", geri arama_verisi=f"duraklatvc {sohbet_kimliği}"),
            InlineKeyboardButton("â–¶ï¸ ", geri_çağrı_verisi=f"resumevc {sohbet_kimliği}"),
            InlineKeyboardButton("â ", geri arama_verisi=f"YÖNETİCİ 2|{sohbet_kimliği}"),
            InlineKeyboardButton("â ¹", geri arama_verisi=f"stopvc {sohbet_kimliği}"),
        ],
        [
            InlineKeyboardButton("ğŸ'Ž Listeye Ekle", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton("âœ¨ Kontrol Paneli", callback_data=f"PanelMarkup Yok|{chat_id}"),
        ],
    ]
    dönüş düğmeleri


# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
# ğŸŒ€ Telegram akışı oynatma
# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
def telegram_markup_timer(_, chat_id, oynatıldı, dur, videoid):
    düğmeler = [
        [InlineKeyboardButton("ğŸš€ ğ ™¿ğ š ğ ™´ğ ™½ğ š‚ğ ™´ğ š‚ á´…á´œÊ á´œÊ€á´œ ğŸš€", url = "https://t.me/prenses_muzik_duyuru")],
        [InlineKeyboardButton(progress_bar(oynatılan, süre), geri_çağrı_verisi="tıklanamayan")],
        [
            InlineKeyboardButton("â ®", geri arama_verisi=f"YÖNETİCİ 1|{sohbet_kimliği}"),
            InlineKeyboardButton("â ¸", geri arama_verisi=f"duraklatvc {sohbet_kimliği}"),
            InlineKeyboardButton("â–¶ï¸ ", geri_çağrı_verisi=f"resumevc {sohbet_kimliği}"),
            InlineKeyboardButton("â ", geri arama_verisi=f"YÖNETİCİ 2|{sohbet_kimliği}"),
            InlineKeyboardButton("â ¹", geri arama_verisi=f"stopvc {sohbet_kimliği}"),
        ],
        [
            InlineKeyboardButton("ğŸ'Ž Listeye Ekle", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton("âœ¨ Kontrol Paneli", callback_data=f"PanelMarkup Yok|{chat_id}"),
        ],
    ]
    dönüş düğmeleri


# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
# ğŸŽ›ï¸ Standart kontrol menüleriÜ¼
# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
def telegram_markup(_, sohbet_kimliği):
    düğmeler = [
        [
            InlineKeyboardButton("â ®", geri arama_verisi=f"YÖNETİCİ 1|{sohbet_kimliği}"),
            InlineKeyboardButton("â ¸", geri arama_verisi=f"duraklatvc {sohbet_kimliği}"),
            InlineKeyboardButton("â–¶ï¸ ", geri_çağrı_verisi=f"resumevc {sohbet_kimliği}"),
            InlineKeyboardButton("â ", geri arama_verisi=f"YÖNETİCİ 2|{sohbet_kimliği}"),
            InlineKeyboardButton("â ¹", geri arama_verisi=f"stopvc {sohbet_kimliği}"),
        ],
        [
            InlineKeyboardButton("ğŸ' Menüye Dün", callback_data=f"PanelMarkup Yok|{chat_id}"),
            InlineKeyboardButton("â Œ Kapat", callback_data="close"),
        ],
    ]
    dönüş düğmeleri


# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
# ğŸ§© Parça seÃ§imi (liste veya sorgu)
# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
def track_markup(_, videoid, kullanıcı_id, kanal, fplay):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_1"], geri arama_verisi=f"MusicStream {videoid}|{user_id}|a|{kanal}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_2"], geri arama_verisi=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [InlineKeyboardButton("â Œ Kapat", geri arama_verisi=f"forceclose {videoid}|{user_id}")],
    ]
    dönüş düğmeleri


# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
# ğŸ“œ Çalma listesi menüsü
# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
def playlist_markup(_, videoid, user_id, ptype, kanal, fplay):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_1"], geri arama_verisi=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_2"], geri arama_verisi=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [InlineKeyboardButton("â Œ Kapat", geri arama_verisi=f"forceclose {videoid}|{user_id}")],
    ]
    dönüş düğmeleri


# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
# ğŸ“º Canlı yayının oynatma menüsü
# â”€â€â”â€â€â€â”€â€â”€â€â€â”€â€â€â€”€â”â€â”€â€â”€â€â”€â€â”€â”€â”€â”â”€â”€â”€â”€â”â”€â”€
def livestream_markup(_, videoid, user_id, mod, kanal, fplay):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_3"],
                callback_data=f"Canlı Yayın {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["MENÜYÜ_KAPATMA_DÜĞMESİ"],
                geri arama_verisi=f"forceclose {videoid}|{kullanıcı_kimliği}",
            ),
        ],
    ]
    dönüş düğmeleri


## Kaydırıcı Sorgu İşaretlemesi


def kaydırıcı_işaretleme(
    _, videoid, kullanıcı_kimliği, sorgu, sorgu_türü, kanal, fplay
):
    sorgu = f"{sorgu[:20]}"
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_1"],
                geri arama_verisi=f"MusicStream {videoid}|{user_id}|a|{kanal}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_2"],
                geri arama_verisi=f"MusicStream {videoid}|{user_id}|v|{kanal}|{fplay}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                metin="â ®",
                geri arama_verisi=f"kaydırıcı B|{sorgu_türü}|{sorgu}|{kullanıcı_kimliği}|{kanal}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["KAPAT_DÜĞMESİ"],
                geri arama_verisi=f"forceclose {sorgu}|{kullanıcı_kimliği}",
            ),
            Satır İçi Klavye Düğmesi(
                metin="â ¯",
                geri arama_verisi=f"kaydırıcı F|{sorgu_türü}|{sorgu}|{kullanıcı_kimliği}|{kanal}|{fplay}",
            ),
        ],
    ]
    dönüş düğmeleri


## Cpanel İşaretlemesi


def panel_markup_1(_, video kimliği, chat_id):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text="â ¸ Duraklat", callback_data=f"YÖNETİCİ Duraklat|{sohbet_kimliği}"
            ),
            Satır İçi Klavye Düğmesi(
                text="â–¶ï¸ Özgeçmiş",
                callback_data=f"YÖNETİCİ Özgeçmişi|{sohbet_kimliği}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                text="â ¯ Atla", callback_data=f"YÖNETİCİ Atla|{chat_id}"
            ),
            Satır İçi Klavye Düğmesi(
                text="â ¹ Durdur", callback_data=f"YÖNETİCİ Durdur|{sohbet_kimliği}"
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                metin="â—€ï¸ ",
                callback_data=f"Sayfalar Geri|0|{videoid}|{chat_id}",
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ”™ Geri",
                geri arama_verisi=f"Anaİşaretleme {videoid}|{sohbet_id}",
            ),
            Satır İçi Klavye Düğmesi(
                metin="â–¶ï¸ ",
                callback_data=f"İleri Sayfalar|0|{videoid}|{sohbet_id}",
            ),
        ],
    ]
    dönüş düğmeleri


def panel_markup_2(_, video kimliği, chat_id):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text="ğŸ”‡ Sessize Al", callback_data=f"YÖNETİCİ Sessize Al|{chat_id}"
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ”Š Sesi Aç",
                callback_data=f"YÖNETİCİ Sessizliği Kaldır|{chat_id}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                text="ğŸ”€ Karıştır",
                callback_data=f"YÖNETİCİ Karıştırma|{sohbet_kimliği}",
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ” Döngüsü", callback_data=f"YÖNETİCİ Döngüsü|{chat_id}"
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                metin="â—€ï¸ ",
                callback_data=f"Sayfalar Geri|1|{videoid}|{chat_id}",
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ”™ Geri",
                geri arama_verisi=f"Anaİşaretleme {videoid}|{sohbet_id}",
            ),
            Satır İçi Klavye Düğmesi(
                metin="â–¶ï¸ ",
                callback_data=f"İleri Sayfalar|1|{videoid}|{sohbet_id}",
            ),
        ],
    ]
    dönüş düğmeleri


def panel_markup_3(_, video kimliği, chat_id):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text="â ® 10 Saniye",
                geri arama_verisi=f"YÖNETİCİ 1|{sohbet_kimliği}",
            ),
            Satır İçi Klavye Düğmesi(
                text="â 10 Saniye",
                geri arama_verisi=f"YÖNETİCİ 2|{sohbet_kimliği}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                text="â ® 30 Saniye",
                geri arama_verisi=f"YÖNETİCİ 3|{sohbet_kimliği}",
            ),
            Satır İçi Klavye Düğmesi(
                text="â 30 Saniye",
                geri arama_verisi=f"YÖNETİCİ 4|{sohbet_kimliği}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                metin="â—€ï¸ ",
                callback_data=f"Sayfalar Geri|2|{videoid}|{chat_id}",
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ”™ Geri",
                geri arama_verisi=f"Anaİşaretleme {videoid}|{sohbet_id}",
            ),
            Satır İçi Klavye Düğmesi(
                metin="â–¶ï¸ ",
                callback_data=f"İleri Sayfalar|2|{videoid}|{sohbet_id}",
            ),
        ],
    ]
    dönüş düğmeleri


def telegram_markup_timer(_, chat_id, oynatıldı, dur, videoid):
    bar = random.choice(seçim)
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text=f"ğ —£ğ —¥ğ —˜ğ —¡ğ —¦ğ —˜ğ —¦ ğ ˜½ğ ™Šğ ™ ğ ™Ž ",
                url=f"https://t.me/prenses_muzik_duyuru"
            )
        ],

        [
            Satır İçi Klavye Düğmesi(
                metin=_["PL_B_2"],
                geri_çağrı_verisi=f"oynatma_listesi_ekle {videoid}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["PL_B_3"],
                callback_data=f"PanelMarkup Yok|{chat_id}",
            ),
        ],
    ]
    dönüş düğmeleri


# Diğer fonksiyonlar aynı kalıyor...



## Zamanlayıcı Çubuğu Olmadan Satır İçi


def stream_markup(_, videoid, chat_id):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text=f"ğ —£ğ —¥ğ —˜ğ —¡ğ —¦ğ —˜ğ —¦ ğ ˜½ğ ™Šğ ™ ğ ™Ž",
                url=f"https://t.me/prenses_muzik_duyuru"
            )
        ],

        [
            Satır İçi Klavye Düğmesi(
                metin=_["PL_B_2"],
                geri_çağrı_verisi=f"oynatma_listesi_ekle {videoid}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["PL_B_3"],
                callback_data=f"PanelMarkup Yok|{chat_id}",
            ),
        ],
    ]
    dönüş düğmeleri


def telegram_markup(_, sohbet_kimliği):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                metin=_["PL_B_3"],
                callback_data=f"PanelMarkup Yok|{chat_id}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["MENÜ_KAPATMA_DÜĞMESİ"], geri_çağrı_verisi="kapat"
            ),
        ],
    ]
    dönüş düğmeleri


## Satır İçi Arama Sorgusu


def track_markup(_, videoid, kullanıcı_id, kanal, fplay):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text=f"ğ —£ğ —¥ğ —˜ğ —¡ğ —¦ğ —˜ğ —¦ ğ ˜½ğ ™Šğ ™ ğ ™Ž",
                url=f"https://t.me/prenses_muzik_duyuru"
            )
        ],

        [
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_1"],
                geri arama_verisi=f"MusicStream {videoid}|{user_id}|a|{kanal}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_2"],
                geri arama_verisi=f"MusicStream {videoid}|{user_id}|v|{kanal}|{fplay}",
            ),
        ],
    ]
    dönüş düğmeleri


def playlist_markup(_, videoid, user_id, ptype, kanal, fplay):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text=f"âš¡ ğ —£ğ —¥ğ —˜ğ —¡ğ —¦ğ —˜ğ —¦ ğ ˜½ğ ™Šğ ™ ğ ™Ž âš¡",
                url=f"https://t.me/prenses_muzik_duyuru"
            )
        ],

        [
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_1"],
                geri arama_verisi=f"ArchMusicÇalma Listeleri {videoid}|{kullanıcı_kimliği}|{ptype}|a|{kanal}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_2"],
                geri arama_verisi=f"ArchMusicÇalma Listeleri {videoid}|{kullanıcı_kimliği}|{ptype}|v|{kanal}|{fplay}",
            ),
        ],
    ]
    dönüş düğmeleri


## Canlı Yayın İşaretlemesi


def livestream_markup(_, videoid, user_id, mod, kanal, fplay):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_3"],
                callback_data=f"Canlı Yayın {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["MENÜYÜ_KAPATMA_DÜĞMESİ"],
                geri arama_verisi=f"forceclose {videoid}|{kullanıcı_kimliği}",
            ),
        ],
    ]
    dönüş düğmeleri


## Kaydırıcı Sorgu İşaretlemesi


def kaydırıcı_işaretleme(
    _, videoid, kullanıcı_kimliği, sorgu, sorgu_türü, kanal, fplay
):
    sorgu = f"{sorgu[:20]}"
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_1"],
                geri arama_verisi=f"MusicStream {videoid}|{user_id}|a|{kanal}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["P_B_2"],
                geri arama_verisi=f"MusicStream {videoid}|{user_id}|v|{kanal}|{fplay}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                metin="â ®",
                geri arama_verisi=f"kaydırıcı B|{sorgu_türü}|{sorgu}|{kullanıcı_kimliği}|{kanal}|{fplay}",
            ),
            Satır İçi Klavye Düğmesi(
                metin=_["KAPAT_DÜĞMESİ"],
                geri arama_verisi=f"forceclose {sorgu}|{kullanıcı_kimliği}",
            ),
            Satır İçi Klavye Düğmesi(
                metin="â ¯",
                geri arama_verisi=f"kaydırıcı F|{sorgu_türü}|{sorgu}|{kullanıcı_kimliği}|{kanal}|{fplay}",
            ),
        ],
    ]
    dönüş düğmeleri


## Cpanel İşaretlemesi


def panel_markup_1(_, video kimliği, chat_id):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text="â ¸ Duraklat", callback_data=f"YÖNETİCİ Duraklat|{sohbet_kimliği}"
            ),
            Satır İçi Klavye Düğmesi(
                text="â–¶ï¸ Özgeçmiş",
                callback_data=f"YÖNETİCİ Özgeçmişi|{sohbet_kimliği}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                text="â ¯ Atla", callback_data=f"YÖNETİCİ Atla|{chat_id}"
            ),
            Satır İçi Klavye Düğmesi(
                text="â ¹ Durdur", callback_data=f"YÖNETİCİ Durdur|{sohbet_kimliği}"
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                metin="â—€ï¸ ",
                callback_data=f"Sayfalar Geri|0|{videoid}|{chat_id}",
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ”™ Geri",
                geri arama_verisi=f"Anaİşaretleme {videoid}|{sohbet_id}",
            ),
            Satır İçi Klavye Düğmesi(
                metin="â–¶ï¸ ",
                callback_data=f"İleri Sayfalar|0|{videoid}|{sohbet_id}",
            ),
        ],
    ]
    dönüş düğmeleri


def panel_markup_2(_, video kimliği, chat_id):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text="ğŸ”‡ Sessize Al", callback_data=f"YÖNETİCİ Sessize Al|{chat_id}"
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ”Š Sesi Aç",
                callback_data=f"YÖNETİCİ Sessizliği Kaldır|{chat_id}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                text="ğŸ”€ Karıştır",
                callback_data=f"YÖNETİCİ Karıştırma|{sohbet_kimliği}",
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ” Döngüsü", callback_data=f"YÖNETİCİ Döngüsü|{chat_id}"
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                metin="â—€ï¸ ",
                callback_data=f"Sayfalar Geri|1|{videoid}|{chat_id}",
            ),
            Satır İçi Klavye Düğmesi(
                text="ğŸ”™ Geri",
                geri arama_verisi=f"Anaİşaretleme {videoid}|{sohbet_id}",
            ),
            Satır İçi Klavye Düğmesi(
                metin="â–¶ï¸ ",
                callback_data=f"İleri Sayfalar|1|{videoid}|{sohbet_id}",
            ),
        ],
    ]
    dönüş düğmeleri


def panel_markup_3(_, video kimliği, chat_id):
    düğmeler = [
        [
            Satır İçi Klavye Düğmesi(
                text="â ® 10 Saniye",
                geri arama_verisi=f"YÖNETİCİ 1|{sohbet_kimliği}",
            ),
            Satır İçi Klavye Düğmesi(
                text="â 10 Saniye",
                geri arama_verisi=f"YÖNETİCİ 2|{sohbet_kimliği}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                text="â ® 30 Saniye",
                geri arama_verisi=f"YÖNETİCİ 3|{sohbet_kimliği}",
            ),
            Satır İçi Klavye Düğmesi(
                text="â 30 Saniye",
                geri arama_verisi=f"YÖNETİCİ 4|{sohbet_kimliği}",
            ),
        ],
        [
            Satır İçi Klavye Düğmesi(
                metin="â—€ï¸ ",
                callback_data=f"Sayfalar Geri|2|{videoid}|{chat_id}",
            ),
            Satır İçi

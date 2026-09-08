# BLACK Apps — Render

Bağımsız Android indirme sitesi. Sessiz Oda 2.0.5 ve Black Sticker Maker 0.1.0 ön sürümü içerir.

## Yayınlama

[Render'da BLACK Apps'i kur](https://render.com/deploy?repo=https://github.com/hiraeth1st/Black-Apps)

Bağlantıyı açın, Render hesabınızla giriş yapın ve Blueprint kurulumunu onaylayın.
Alternatif: Render → New → Blueprint → hiraeth1st/Black-Apps deposunu seçin.
`render.yaml` yalnızca BLACK Apps statik sitesini oluşturur; mevcut sohbet sunucusunu değiştirmez.

Manuel alternatif: New → Static Site → depo → branch main.
Build Command: `python3 verify.py`
Publish Directory: `dist`
Ortam değişkeni ve kalıcı disk gerekmez. Blueprint APK indirme başlıklarını da ayarlar.

## Güncelleme

Yeni doğrulanmış APK ve SHA-256 dosyasını dist/downloads/ içine ekleyin.
dist/index.html içindeki bağlantı, sürüm ve boyutu güncelleyin.
GitHub'a gönderilen güncellemeleri Render bağlı servisin otomatik deploy ayarına göre yayımlar.
Bu site GitHub release'lerini otomatik çekmez.

Simgeler uygulamaların kendi vector kaynaklarından dönüştürüldü.
APK'lar yayımlanmış sürümlerle byte düzeyinde aynıdır.
İmza anahtarları ve sunucu sırları bu pakette bulunmaz.

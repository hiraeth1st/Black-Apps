# BLACK Apps — Render

Bağımsız Android indirme sitesi. Sessiz Oda 2.0.5, Black Sticker Maker 0.1.0 ve Black Video 1.0.0 ön sürümlerini içerir.

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

## Black Video dağıtımı

Black Video APK 107.539.078 bayttır ve GitHub tek dosya sınırını aşar. Bu yüzden APK GitHub Release v1.0.0 içinde saklanır. Render derlemesinde verify.py, downloads.json içindeki sabit bağlantıdan indirir; boyutunu ve SHA-256 değerini kontrol ettikten sonra dist/downloads/black-video-1.0.0.apk olarak yayımlar. Hatalı veya eksik dosya varsa derleme başarısız olur. Ziyaretçi APK’yı doğrudan bu siteden indirir. Secret veya yeni ortam değişkeni gerekmez.

Kaynak commit: 7adf514b6f6c41b1197f208ccebd9e2c67c71403; başarılı Actions run: 34231337561. Paket yeniden imzalanmadı. GPL-3.0 lisansı ve kaynak kodu bağlantısı uygulama kartında sunulur.

Sürüm yükseltirken downloads.json, SHA-256 dosyası ve uygulama kartı birlikte güncellenmelidir. Release silinirse sonraki site derlemesi durur; son başarılı yayın etkilenmez.

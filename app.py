import streamlit as st
import os

# ----------------- SAYFA AYARLARI -----------------
# Streamlit sayfasının temel yapılandırmasını ayarlar.
# 'wide' modu sayfanın tüm genişliği kullanmasını sağlar.
st.set_page_config(
    layout="wide",
    page_title="Elden Taksit Başvuru Formu",
    page_icon="📝"
)

# ----------------- ANA BAŞLIK VE AÇIKLAMA -----------------
st.title("📝 Elden Taksit Başvuru Formu")
st.markdown("Hayalinizdeki ürüne kolayca sahip olmak için aşağıdaki başvuru formunu doldurmanız yeterlidir.")
st.markdown("---")

# ----------------- HTML FORMUNU YÜKLEME -----------------

# Gösterilecek HTML dosyasının adı.
# Bu dosyanın app.py ile aynı klasörde olması beklenir.
HTML_FORM_FILE = "form.html"

def load_html_file(file_path):
    """Belirtilen yoldaki HTML dosyasını okur ve içeriğini döndürür."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

# HTML dosyasının tam yolunu al
html_path = os.path.join(os.path.dirname(__file__), HTML_FORM_FILE)

# HTML içeriğini yükle
html_code = load_html_file(html_path)

if html_code:
    # HTML kodunu bir Streamlit bileşeni olarak sayfaya ekle.
    # height: iframe'in yüksekliğini belirler.
    # scrolling=True: Gerekirse iframe içinde kaydırma çubuğu çıkmasını sağlar.
    st.components.v1.html(html_code, height=700, scrolling=True)
else:
    # HTML dosyası bulunamazsa kullanıcıyı bilgilendir.
    st.error(f"HATA: '{HTML_FORM_FILE}' dosyası bulunamadı!")
    st.warning(
        f"Lütfen Canvas'taki HTML kodunu kopyalayıp bu Python betiğiyle "
        f"aynı klasörde '{HTML_FORM_FILE}' adıyla kaydedin."
    )

# ----------------- YAN MENÜ (SIDEBAR) BİLGİLENDİRMESİ -----------------
st.sidebar.header("Kullanım Adımları")
st.sidebar.markdown(
    """
    Bu uygulamayı çalıştırmak için:

    1.  **HTML Dosyasını Oluşturun:**
        * Canvas'taki HTML kodunun tamamını kopyalayın.
        * Bu `app.py` dosyasıyla aynı klasörde `form.html` adında yeni bir dosya oluşturup içine yapıştırın.

    2.  **Google Form'u Ayarlayın:**
        * Oluşturduğunuz `form.html` dosyasını bir metin düzenleyici ile açın.
        * `SİZİN_GOOGLE_FORM_YANIT_URL_NİZ` yazan yeri ve `entry.ID`'leri kendi Google Form bilgilerinizle güncelleyin.

    3.  **Uygulamayı Başlatın:**
        * Terminal veya komut istemcisini açın.
        * Aşağıdaki komutu çalıştırın:
        ```bash
        streamlit run app.py
        ```
    """
)
st.sidebar.info("Form gönderildikten sonra verileriniz ayarladığınız Google E-Tablolar dosyasına kaydedilecektir.")

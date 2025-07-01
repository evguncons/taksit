import streamlit as st
import os

# ----------------- SAYFA AYARLARI -----------------
# Streamlit sayfasının temel yapılandırmasını ayarlar.
# 'wide' modu sayfanın tüm genişliği kullanmasını sağlar.
st.set_page_config(
    layout="wide",
    page_title="Elden Taksit Başvuru Formu"
)

# --- Streamlit'in varsayılan üst ve yan boşluklarını kaldırmak için CSS ---
# Bu kod, formun sayfayı tam olarak kaplamasını sağlar.
st.markdown("""
    <style>
        /* Ana uygulama alanındaki tüm dolguları (padding) kaldır */
        .main .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        /* Streamlit'in üstbilgisini (header) ve menüsünü gizle */
        header {
            visibility: hidden;
        }
        #MainMenu {
            visibility: hidden;
        }
        /* Streamlit'in altbilgisini (footer) gizle */
        footer {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True)


# ----------------- HTML FORMUNU YÜKLEME -----------------

# Gösterilecek HTML dosyasının adı.
# Bu dosyanın app.py ile aynı klasörde olması gerekir.
HTML_FORM_FILE = "form.html"

def load_html_file(file_path):
    """Belirtilen yoldaki HTML dosyasını okur ve içeriğini döndürür."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

# HTML dosyasının tam yolunu al
# __file__ mevcut betiğin yolunu belirtir, bu sayede dosya yolu her zaman doğru olur.
html_path = os.path.join(os.path.dirname(__file__), HTML_FORM_FILE)

# HTML içeriğini yükle
html_code = load_html_file(html_path)

if html_code:
    # HTML kodunu bir Streamlit bileşeni olarak sayfaya ekle.
    # Yükseklik, dikey kaydırma çubuğu oluşmaması için yeterince büyük ayarlandı.
    st.components.v1.html(html_code, height=900, scrolling=False)
else:
    # HTML dosyası bulunamazsa, kullanıcıyı bilgilendirmek için bir hata mesajı göster.
    st.error(f"HATA: '{HTML_FORM_FILE}' dosyası bulunamadı!")
    st.warning(
        f"Lütfen Canvas'taki HTML kodunu kopyalayıp bu Python betiğiyle "
        f"aynı klasörde '{HTML_FORM_FILE}' adıyla kaydedin."
    )

import streamlit as st
import os

# ----------------- SAYFA AYARLARI -----------------
# Streamlit sayfasının temel yapılandırmasını ayarlar.
st.set_page_config(
    layout="wide",
    page_title="Elden Taksit Başvuru Formu"
)

# --- Streamlit Arayüzünü ve Boşlukları Kaldırmak için CSS ---
# Bu kod, formun sayfayı tam olarak kaplaması için Streamlit'in
# varsayılan stillerini geçersiz kılar.
st.markdown("""
    <style>
        /* Streamlit'in ana uygulama kapsayıcısındaki tüm boşlukları kaldır */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Daha genel bir seçici ile tüm üst düzey boşlukları hedefle */
        div[data-testid="stAppViewContainer"] > .main > div:first-child {
             padding: 0;
        }

        /* Streamlit'in üstbilgisini (header) tamamen gizle */
        header {
            visibility: hidden;
            height: 0;
        }

        /* Hamburger menüsünü tamamen gizle */
        #MainMenu {
            visibility: hidden;
        }

        /* Streamlit'in altbilgisini (footer) tamamen gizle */
        footer {
            visibility: hidden;
        }
        
        /* Sağ üstteki araç çubuğunu gizle */
        div[data-testid="stToolbar"] {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True)


# ----------------- HTML FORMUNU YÜKLEME -----------------

# Gösterilecek HTML dosyasının adı.
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
    # Yükseklik, dikey kaydırma çubuğu oluşmaması için yeterince büyük ayarlandı.
    st.components.v1.html(html_code, height=1024, scrolling=True)
else:
    # HTML dosyası bulunamazsa, kullanıcıyı bilgilendirmek için bir hata mesajı göster.
    st.error(f"HATA: '{HTML_FORM_FILE}' dosyası bulunamadı!")
    st.warning(
        f"Lütfen Canvas'taki güncel HTML kodunu kopyalayıp bu Python betiğiyle "
        f"aynı klasörde '{HTML_FORM_FILE}' adıyla kaydedin."
    )

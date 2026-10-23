import streamlit as st

# ==========================================
# CONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Materi Pramuka Indonesia - Mustafa Abdul Ghofur",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS (Tema Warna Cokelat, Krem, Emas & Watermark Elegan)
# ==========================================
st.markdown("""
    <style>
    /* Theme Colors & Fonts */
    :root {
        --primary-brown: #4A2E1A;
        --secondary-brown: #6F4E37;
        --accent-gold: #D4AF37;
        --bg-krem: #FDFBF7;
    }
    
    .stApp {
        background-color: var(--bg-krem);
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Card */
    .hero-card {
        background: linear-gradient(135deg, #4A2E1A 0%, #2A180D 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        border: 2px solid #D4AF37;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        color: #D4AF37;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    /* Section Cards */
    .material-card {
        background-color: white;
        padding: 1.8rem;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 6px solid #D4AF37;
        margin-bottom: 1.5rem;
    }
    
    .card-title {
        color: #4A2E1A;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Watermark Footer */
    .watermark-footer {
        position: relative;
        bottom: 0;
        width: 100%;
        background-color: #4A2E1A;
        color: #D4AF37;
        text-align: center;
        padding: 1.2rem;
        border-top: 3px solid #D4AF37;
        font-weight: 600;
        font-size: 0.95rem;
        margin-top: 3rem;
        border-radius: 12px;
        letter-spacing: 0.5px;
    }

    /* Badge Style */
    .badge-tag {
        background-color: rgba(212, 175, 55, 0.2);
        color: #4A2E1A;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        border: 1px solid #D4AF37;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/e/e6/Gerakan_Pramuka_Indonesia_logo.svg", width=120)
st.sidebar.title("⚜️ Navigasi Materi")
menu = st.sidebar.radio(
    "Pilih Pembahasan:",
    [
        "🏛️ Sejarah & Tokoh",
        "📜 Kode Kehormatan",
        "🎒 Tingkatan Pramuka",
        "🎗️ Salam & Lambang",
        "📻 Sandi & Morse",
        "🏆 SKU & TKK",
        "🎯 Kuis Interaktif"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Website Pembelajaran Resmi**\nDibuat untuk menyajikan materi Gerakan Pramuka Indonesia secara interaktif.")

# ==========================================
# MAIN CONTENT
# ==========================================

# Hero Banner
st.markdown("""
    <div class="hero-card">
        <div class="hero-title">PORTAL PRAMUKA INDONESIA</div>
        <p style="font-size: 1.1rem; opacity: 0.9;">Setya Kudharma Kencana — Edukasi & Khazanah Kepramukaan Lengkap</p>
    </div>
""", unsafe_allow_html=True)

# 1. SEJARAH & TOKOH
if menu == "🏛️ Sejarah & Tokoh":
    st.header("🏛️ Sejarah & Tokoh Pramuka Indonesia")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="material-card">
            <div class="card-title">Sejarah Ringkas Gerakan Pramuka</div>
            <p>Gerakan Pramuka di Indonesia dimulai sejak tahun 1912 dengan berdirinya organisasi milik Belanda bernama <i>Nederlandsche Padtvinders Organisatie (NPO)</i> yang kemudian berganti menjadi <i>NIPV</i>.</p>
            <p>Tokoh-tokoh pergerakan nasional kemudian membentuk organisasi kepanduan sendiri seperti JPO (Jawaansche Padvinders Organizatie), JJP, NATIPIJ, dan lainnya.</p>
            <p>Pada <b>14 Agustus 1961</b>, seluruh organisasi kepanduan di Indonesia dilebur menjadi satu wadah tunggal bernama <b>Gerakan Pramuka</b> melalui Keputusan Presiden RI No. 238 Tahun 1961. Peristiwa inilah yang diperingati sebagai <b>Hari Pramuka</b>.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="material-card" style="border-left-color: #8B0000;">
            <div class="card-title">👑 Bapak Pramuka Indonesia</div>
            <p><b>Sri Sultan Hamengkubuwono IX</b></p>
            <hr>
            <p style="font-size: 0.9rem;">Beliau adalah Ketua Kwartir Nasional (Ka Kwarnas) pertama yang menjabat dari tahun 1961 hingga 1974 dan dianugerahi gelar <b>Bapak Pramuka Indonesia</b> atas jasa-jasanya menyatukan gerakan kepanduan.</p>
        </div>
        """, unsafe_allow_html=True)

# 2. KODE KEHORMATAN
elif menu == "📜 Kode Kehormatan":
    st.header("📜 Kode Kehormatan Pramuka")
    
    tab1, tab2 = st.tabs(["Tri Satya (Janji)", "Dasa Darma (Ketentuan Moral)"])
    
    with tab1:
        st.markdown("""
        <div class="material-card">
            <div class="card-title">TRI SATYA</div>
            <p><i>Demi kehormatanku aku berjanji akan bersungguh-sungguh:</i></p>
            <ol>
                <li><b>Menjalankan kewajibanku</b> terhadap Tuhan, Negara Kesatuan Republik Indonesia dan mengamalkan Pancasila.</li>
                <li><b>Menolong sesama hidup</b> dan ikut serta membangun masyarakat.</li>
                <li><b>Menepati Dasa Darma.</b></li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
        <div class="material-card">
            <div class="card-title">DASA DARMA PRAMUKA</div>
            <p>Pramuka itu:</p>
            <ol>
                <li><b>Taqwa</b> kepada Tuhan Yang Maha Esa.</li>
                <li><b>Cinta alam</b> dan kasih sayang sesama manusia.</li>
                <li><b>Patriot</b> yang sopan dan kesatria.</li>
                <li><b>Patuh</b> dan suka bermusyawarah.</li>
                <li><b>Rela menolong</b> dan tabah.</li>
                <li><b>Rajin</b>, terampil, dan gembira.</li>
                <li><b>Hemat</b>, cermat, dan bersahaja.</li>
                <li><b>Disiplin</b>, berani, dan setia.</li>
                <li><b>Bertanggung jawab</b> dan dapat dipercaya.</li>
                <li><b>Suci</b> dalam pikiran, perkataan, dan perbuatan.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

# 3. TINGKATAN PRAMUKA
elif menu == "🎒 Tingkatan Pramuka":
    st.header("🎒 Tingkatan Anggota Pramuka")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("""
        <div class="material-card" style="border-left-color: #16a34a;">
            <div class="card-title">1. Siaga <span class="badge-tag">Usia 7 - 10 Tahun</span></div>
            <ul>
                <li><b>Satuan Terkecil:</b> Barung (dipimpin Pinru)</li>
                <li><b>Kumpulan Barung:</b> Perindukan</li>
                <li><b>Tingkatan TKU:</b> Mula, Bantu, Tata</li>
                <li><b>Warna Khas:</b> Hijau</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="material-card" style="border-left-color: #dc2626;">
            <div class="card-title">2. Penggalang <span class="badge-tag">Usia 11 - 15 Tahun</span></div>
            <ul>
                <li><b>Satuan Terkecil:</b> Regu (dipimpin Pinru, Pemimpin Utama = Pratama)</li>
                <li><b>Kumpulan Regu:</b> Pasukan</li>
                <li><b>Tingkatan TKU:</b> Ramu, Rakit, Terap</li>
                <li><b>Warna Khas:</b> Merah</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="material-card" style="border-left-color: #eab308;">
            <div class="card-title">3. Penegak <span class="badge-tag">Usia 16 - 20 Tahun</span></div>
            <ul>
                <li><b>Satuan Terkecil:</b> Sangga (dipimpin Pinsa, Pemimpin Utama = Pradana)</li>
                <li><b>Kumpulan Sangga:</b> Ambalan</li>
                <li><b>Tingkatan TKU:</b> Bantara, Laksana</li>
                <li><b>Warna Khas:</b> Kuning / Emas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="material-card" style="border-left-color: #4A2E1A;">
            <div class="card-title">4. Pandega <span class="badge-tag">Usia 21 - 25 Tahun</span></div>
            <ul>
                <li><b>Satuan Terkecil:</b> Reka</li>
                <li><b>Kumpulan Reka:</b> Racana</li>
                <li><b>Tingkatan TKU:</b> Pandega</li>
                <li><b>Warna Khas:</b> Cokelat Tua</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# 4. SALAM & LAMBANG
elif menu == "🎗️ Salam & Lambang":
    st.header("🎗️ Salam & Lambang Gerakan Pramuka")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="material-card">
            <div class="card-title">3 Jenis Salam Pramuka</div>
            <ul>
                <li><b>Salam Biasa:</b> Diberikan kepada sesama anggota Pramuka tanpa memandang kedudukan (posisi berdiri tegak/duduk).</li>
                <li><b>Salam Penghormatan:</b> Diberikan kepada pejabat/tokoh (Presiden, Bendera Merah Putih, Lagu Indonesia Raya, Jenazah).</li>
                <li><b>Salam Janji:</b> Diberikan saat anggota Pramuka dilantik dan mengucapkan Tri Satya.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="material-card">
            <div class="card-title">Lambang Tunas Kelapa</div>
            <p>Diciptakan oleh <b>Sunardjo Atmodipuro</b>. Makna dibalik lambang:</p>
            <ul>
                <li><b>Cikal/Tunas:</b> Cikal bakal generasi penerus bangsa.</li>
                <li><b>Dapat Tumbuh Dimana Saja:</b> Daya adaptasi tinggi di berbagai kondisi.</li>
                <li><b>Pohon Menjulang Lurus:</b> Memiliki cita-cita lurus, tinggi, dan jujur.</li>
                <li><b>Akar Kuat:</b> Menancap pada landasan iman dan moral yang kuat.</li>
                <li><b>Pohon Serbaguna:</b> Setiap bagian berguna bagi masyarakat.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# 5. SANDI & MORSE
elif menu == "📻 Sandi & Morse":
    st.header("📻 Sandi, Morse & Semaphore")
    
    st.markdown("""
    <div class="material-card">
        <div class="card-title">Isyarat & Komunikasi Kerahasiaan</div>
        <p>Dalam kepramukaan, komunikasi jarak jauh dan keamanan pesan dipelajari melalui berbagai teknik:</p>
        <ol>
            <li><b>Kode Morse:</b> Diciptakan oleh Samuel Morse. Disampaikan melalui peluit, senter, atau ketukan. (Contoh: S = <code>...</code>, O = <code>---</code>).</li>
            <li><b>Sandi Rumput:</b> Turunan dari Kode Morse, di mana titik (<code>.</code>) digambarkan dengan rumput pendek dan garis (<code>-</code>) dengan rumput tinggi.</li>
            <li><b>Semaphore:</b> Isyarat menggunakan sepasang bendera berukuran 45x45 cm berwarna merah dan kuning, dimainkan dengan posisi kedua tangan.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# 6. SKU & TKK
elif menu == "🏆 SKU & TKK":
    st.header("🏆 SKU, SKK, TKK & Pramuka Garuda")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("""
        <div class="material-card">
            <div class="card-title">SKU & TKU</div>
            <p><b>Syarat Kecakapan Umum (SKU)</b> adalah syarat wajib yang harus dipenuhi anggota untuk mendapatkan <b>Tanda Kecakapan Umum (TKU)</b> sesuai tingkatan (Ramu, Bantara, dll).</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="material-card">
            <div class="card-title">TKK (Tanda Kecakapan Khusus)</div>
            <p>Diberikan atas keahlian bidang tertentu (Masak, Qori, Kemah, dll).</p>
            <p>Tingkatan TKK: <b>Purwa</b> (Lingkaran), <b>Madya</b> (Persegi), <b>Utama</b> (Segilima).</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.success("🌟 **Pramuka Garuda** adalah tingkatan kecakapan tertinggi dalam setiap golongan Pramuka yang mencerminkan keteladanan dan kecakapan di atas rata-rata.")

# 7. KUIS INTERAKTIF
elif menu == "🎯 Kuis Interaktif":
    st.header("🎯 Kuis Pengetahuan Pramuka")
    
    questions = [
        {"q": "1. Siapakah yang dianugerahi sebagai Bapak Pramuka Indonesia?", "options": ["Baden Powell", "Sunardjo Atmodipuro", "Sri Sultan Hamengkubuwono IX", "Soekarno"], "a": "Sri Sultan Hamengkubuwono IX"},
        {"q": "2. Pencipta lambang Tunas Kelapa adalah...", "options": ["KH Agus Salim", "Sunardjo Atmodipuro", "Ki Hajar Dewantara", "R.A. Kartini"], "a": "Sunardjo Atmodipuro"},
        {"q": "3. Anggota Pramuka berumur 11 sampai 15 tahun tergolong dalam tingkat...", "options": ["Siaga", "Penggalang", "Penegak", "Pandega"], "a": "Penggalang"},
        {"q": "4. Satuan terkecil dalam golongan Pramuka Penegak disebut...", "options": ["Barung", "Regu", "Sangga", "Reka"], "a": "Sangga"},
        {"q": "5. 'Taqwa kepada Tuhan Yang Maha Esa' adalah Dasa Darma ke-...", "options": ["1", "2", "3", "5"], "a": "1"}
    ]
    
    score = 0
    with st.form("quiz_form"):
        answers = []
        for idx, item in enumerate(questions):
            st.subheader(item["q"])
            ans = st.radio("Pilih jawaban:", item["options"], key=f"q_{idx}")
            answers.append((ans, item["a"]))
            st.markdown("---")
            
        submitted = st.form_submit_button("Submit Jawaban")
        
        if submitted:
            for ans, correct in answers:
                if ans == correct:
                    score += 20
            
            st.balloons()
            st.success(f"🎉 Kuis Selesai! Skor Anda: **{score} / 100**")
            if score == 100:
                st.info("Sempurna! Pengetahuan Kepramukaan Anda Sangat Luar Biasa!")

# ==========================================
# WATERMARK FOOTER (MANDATORY REQUIREMENT)
# ==========================================
st.markdown("""
    <div class="watermark-footer">
        Website Materi Pramuka Indonesia © Mustafa Abdul Ghofur - Calon Pramuka Garuda
    </div>
""", unsafe_allow_html=True)
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("DB_NAME", "fess") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001979450020"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001721745890")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1001637096480"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "732448606"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "2"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "50"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#111 #112 #fwbboy #fwbgirl #fwbspill #fwbask #fwbstory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
kamu tidak dapat menggunakan bot 🙅, untuk mengirim pesan ke @fwb18fess harap join terlebih dahulu ke channel dan grup yang ada dibawah, jika sudah tekan coba lagi atau /help.

Seputar informasi & pertanyaan hubungi @leoservicebot
""")
start_msg = os.getenv("START_MSG", """
halo {mention}

💬 Sender 18+ Fwb adalah bot promote yang dapat digunakan untuk mencari teman, pacar, fwb dll serta dapat digunakan untuk mengirim pap/video randommu, gunakan hastag dibawah untuk mengirim pesan:

#fwbboy : untuk mencari teman jika kamu seorang cowo.
#fwbgirl : untuk mencari teman jika kamu seorang cewe.
#fwbspill : untuk spill sesuatu.
#fwbstory : untuk berbagi cerita/pengalaman.
#fwbask : untuk bertanya ke grup.
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#fwbboy : untuk mencari teman jika kamu seorang cowo.
#fwbgirl : untuk mencari teman jika kamu seorang cewe.
#fwbspill : untuk spill sesuatu.
#fwbstory : untuk berbagi cerita/pengalaman.
#fwbask : untuk bertanya ke grup.

powered by @topbasetelegram
""")

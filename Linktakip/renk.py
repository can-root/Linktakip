# https://github.com/can-root
class renk:
    KIRMIZI = "\033[91m"
    SARI = "\033[93m"
    YESIL = "\033[92m"
    MOR = "\033[95m"
    TURUNCU = "\033[38;5;214m"
    GRI = "\033[90m"
    MAVI = "\033[94m"
    CG = "\033[96m"
    BEYAZ = "\033[97m"
    SIYAH = "\033[30m"
    KAHVERENGI = "\033[38;5;94m"
    PEMBE = "\033[38;5;13m"
    LACIVERT = "\033[38;5;24m"
    FUSYA = "\033[38;5;199m"
    KAHVE = "\033[38;5;130m"

    BG_KIRMIZI = "\033[41m"
    BG_SARI = "\033[43m"
    BG_YESIL = "\033[42m"
    BG_MOR = "\033[45m"
    BG_TURUNCU = "\033[48;5;214m"
    BG_GRI = "\033[100m"
    BG_MAVI = "\033[44m"
    BG_CG = "\033[46m"
    BG_BEYAZ = "\033[107m"
    BG_SIYAH = "\033[40m"
    BG_KAHVERENGI = "\033[48;5;94m"
    BG_PEMBE = "\033[48;5;13m"
    BG_LACIVERT = "\033[48;5;24m"
    BG_FUSYA = "\033[48;5;199m"
    BG_KAHVE = "\033[48;5;130m"

    OFF = "\033[0m"

    @staticmethod
    def renklendir(metin: str) -> str:
        for renk_adi in dir(renk):
            if not renk_adi.startswith("__") and renk_adi != "renklendir":
                metin = metin.replace(f"{{renk.{renk_adi}}}", getattr(renk, renk_adi))
                if renk_adi.startswith("BG_"):
                    arka_renk_adi = renk_adi[3:]
                    metin = metin.replace(f"{{renk.arka.{arka_renk_adi}}}", getattr(renk, renk_adi))

        return metin + renk.OFF

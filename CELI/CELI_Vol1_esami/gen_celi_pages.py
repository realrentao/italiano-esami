# -*- coding: utf-8 -*-
"""Generatore delle 6 pagine d'esame CELI (Vol.1, A1-C2).
Legge i dati strutturati in DATA, genera l'audio TTS (edge-tts) e produce
6 HTML autonomi + index.html nella cartella CELI_Vol1_esami/.
"""
import os, asyncio, html, re, random, hashlib

OUT = r"D:\workbuddy工作区\2026-07-10-17-59-50\CELI_Vol1_esami"
VOICE = "it-IT-ElsaNeural"

def esc(s):
    return html.escape(str(s), quote=True)

# ---------------------------------------------------------------------------
# Audio: genera file .mp3 esterni (più affidabile dei data-URI base64)
# ---------------------------------------------------------------------------
AUDIO_DIR = os.path.join(OUT, "audio")

def audio_path(key):
    return os.path.join(AUDIO_DIR, key + ".mp3")

async def gen_one(text, key, rate="+0%"):
    try:
        import edge_tts
        comm = edge_tts.Communicate(text, VOICE, rate=rate)
        buf = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                buf += chunk["data"]
        os.makedirs(AUDIO_DIR, exist_ok=True)
        with open(audio_path(key), "wb") as f:
            f.write(buf)
        print("AUDIO OK", key, len(buf))
    except Exception as e:
        print("AUDIO FAIL", key, repr(e))

# 口语参考答案语速：等级越低稍慢，更自然易跟读
ORAL_RATE = {"A1": "-12%", "A2": "-8%", "B1": "-5%", "B2": "-3%", "C1": "+0%", "C2": "+0%"}

def gen_all(levels):
    async def run():
        for lv in levels:
            code = lv["code"]
            # 听力音频（已存在则跳过，避免重复联网生成）
            for i, sc in enumerate(lv.get("audio", [])):
                key = "%s_%d" % (code, i)
                if os.path.exists(audio_path(key)):
                    print("AUDIO SKIP", key)
                    continue
                await gen_one(sc["body"], key)
            # 口语参考答案音频
            rate = ORAL_RATE.get(code, "+0%")
            for sec in lv.get("sections", []):
                if sec.get("kind") != "oral":
                    continue
                for i, tk in enumerate(sec.get("tasks", [])):
                    if not tk.get("ref"):
                        continue
                    key = "%s_oral_%d" % (code, i)
                    if os.path.exists(audio_path(key)):
                        print("AUDIO SKIP", key)
                        continue
                    await gen_one(tk["ref"], key, rate)
    try:
        asyncio.run(run())
    except Exception as e:
        print("ASYNC FAIL", repr(e))

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------
LEVELS = []

# ============================== A1 =========================================
LEVELS.append({
    "code": "A1", "name": "CELI Impatto", "subtitle": "la mia città pulita / riciclare a casa",
    "theme": "🌱 Ambiente, clima e sostenibilità", "subj_max": 20,
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo 1 — Avviso（通知）", "body":
"""AVVISO – LA CITTÀ È PULITA!
Ogni lunedì e venerdì raccogliamo la carta.
Ogni martedì e sabato raccogliamo la plastica.
Per favore, metti i rifiuti fuori di casa la sera.
Grazie!
Comune di Verdi"""},
            {"title": "Testo 2 — Messaggio（朋友留言）", "body":
"""Ciao Marco!
Sabato vado al parco con la mia famiglia.
Puliamo il parco insieme. Porta una busta grande!
A presto,
Luca"""},
            {"title": "Testo 3 — Pubblicità（广告）", "body":
"""RICICLA A CASA
Hai vecchie bottiglie? Mettile nel bidone giallo.
Hai giornali vecchi? Mettili nel bidone blu.
È facile e utile per la città!"""},
         ],
         "items": [
            {"type": "match", "prompt": "1. Lunedì e venerdì →", "options": ["la plastica", "la carta"], "answer": 1},
            {"type": "match", "prompt": "2. Martedì e sabato →", "options": ["la plastica", "la carta"], "answer": 0},
            {"type": "mc", "prompt": "3. Dove mettiamo le bottiglie di plastica?", "options": ["nel bidone blu", "nel bidone giallo", "nel bidone verde"], "answer": 1},
            {"type": "mc", "prompt": "4. Cosa fa Luca sabato?", "options": ["pulisce il parco", "compra il latte", "va a scuola"], "answer": 0},
            {"type": "mc", "prompt": "5. Quando mettiamo i rifiuti fuori di casa?", "options": ["la mattina", "la sera", "a mezzogiorno"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Scrivi una cartolina（明信片 / 留言）",
             "prompt": "Scrivi una cartolina a un tuo amico e parla della tua città pulita o del riciclo a casa.（写一张明信片给朋友，谈谈你干净的城市或在家回收。）",
             "limit": "30–50 词",
             "reference":
"""Cara Giulia,
La mia città è molto pulita! A casa riciclo la carta e la plastica.
Ogni sera metto i rifiuti fuori. È facile e utile per tutti.
Un bacio,
Sara"""},
         ]},
        {"kind": "oral", "title": "3. Prova orale（口语，含听力评定）",
         "tasks": [
            {"desc":
"""CELI A1 无独立听力卷，听力能力并入口语评定。考官在互动中即时判断考生对简单指令与提问的理解。
① 考官引导问答（姓名 / 年龄 / 住址 / 家庭 / 日常）；② 简单表达。
示例问句：
1. Come ti chiami?
2. Quanti anni hai? / Dove abiti?
3. Ricicli a casa? Cosa ricicli?（纸／塑料／玻璃？）
4. La tua città è pulita? Perché sì / no?
5. Cosa fai per la tua città?（es. pulisco il parco）""",
             "points": 20,
             "rubric":
"""① 能听懂简单指令并反应（听力并入）；② 用基本词汇与单句作答；③ 发音可懂、语调自然；④ 互动积极、能维持简短交流。达到 11 分即通过。""",
             "dims": [
                ("Pronuncia 发音", "单音基本准确，语调自然，能听懂简单指令"),
                ("Fluenza 流利度", "能用基本词汇与单句作答，无明显长时间停顿"),
                ("Grammatica 语法", "使用基础句型（essere/avere/ presente），错误不影响理解"),
                ("Contenuto 内容", "覆盖姓名 / 年龄 / 住址 / 习惯等任务要求"),
                ("Interazione 互动", "能回应考官提问，维持简短交流"),
             ],
             "ref":
"""Buongiorno, mi chiami Sara. Ho vent'anni e abito a Milano con la mia famiglia. A casa riciclo la carta e la plastica, e ogni mattina porto la borsa di tela al mercato. La mia città è pulita perché tutti noi aiutiamo. Secondo me è importante ridurre la plastica per il futuro. E tu, cosa fai per l'ambiente?"""},
         ]},
    ],
})

# ============================== A2 =========================================
LEVELS.append({
    "code": "A2", "name": "CELI 1", "subtitle": "ridurre la plastica / un parco naturale",
    "theme": "🌱 Ambiente, clima e sostenibilità", "subj_max": 30,
    "audio": [
        {"title": "Dialogo — Compra di una borsa riutilizzabile", "body":
"""Commessa: Buongiorno! Cerchi qualcosa?
Cliente: Sì, vorrei una borsa riutilizzabile. Quante ne hai?
Commessa: Ne ho di tela e di juta. Costa 2 euro.
Cliente: Prendo quella di tela, grazie."""},
        {"title": "Racconto — Al parco", "body":
"""La scorsa domenica sono andata al parco con mio fratello. Abbiamo portato la colazione e abbiamo raccolto la spazzatura per terra. Eravamo contenti perché il parco era più pulito."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，权重 25%）",
         "texts": [
            {"title": "Testo 1 — Blog（短博客）", "body":
"""Il mio impegno contro la plastica
Ciao a tutti! Da un mese uso una borraccia di metallo e non compro più bottiglie di plastica. Porto sempre la mia borsa di tela al supermercato. Ridurre la plastica è facile se iniziamo da piccole cose. E voi, cosa fate?"""},
            {"title": "Testo 2 — Avviso（自然公园通知）", "body":
"""Parco Naturale del Lago
Aperto tutti i giorni 9:00–18:00
Sentieri per camminare e osservare gli uccelli
Vietato lasciare rifiuti – Biglietto: 3 euro"""},
            {"title": "Testo 3 — Pubblicità（广告）", "body":
"""BOTTIGLIE ADDIO!
Compri una borraccia riutilizzabile e risparmi 100 euro all'anno.
Disponibile in due colori: blu e verde."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Da quanto tempo l'autrice usa la borraccia?", "options": ["un anno", "un mese", "una settimana"], "answer": 1},
            {"type": "mc", "prompt": "2. Cosa porta al supermercato?", "options": ["la borraccia", "la borsa di tela", "la bottiglia"], "answer": 1},
            {"type": "mc", "prompt": "3. Il parco è aperto…", "options": ["solo di domenica", "tutti i giorni", "solo la mattina"], "answer": 1},
            {"type": "mc", "prompt": "4. Quanto costa il biglietto del parco?", "options": ["3 euro", "5 euro", "gratis"], "answer": 0},
            {"type": "mc", "prompt": "5. Nel parco è vietato…", "options": ["camminare", "osservare uccelli", "lasciare rifiuti"], "answer": 2},
            {"type": "mc", "prompt": "6. Con la borraccia risparmi…", "options": ["50 euro", "100 euro", "200 euro"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 15%）",
         "tasks": [
            {"title": "Compito 1 — Completamenti（补全短文）",
             "prompt": "Per ridurre la plastica a casa, io uso ____________ (1) invece delle bottiglie. Porto la ____________ (2) al mercato e non prendo le ____________ (3) di plastica. È un piccolo ____________ (4) per l'ambiente.",
             "limit": "填空",
             "reference": "(1) una borraccia；(2) borsa di tela；(3) buste；(4) aiuto / passo"},
            {"title": "Compito 2 — Espansione（扩写为 50–80 词）",
             "prompt": "Espandi il seguente messaggio in 50–80 parole: \"Domani vado al Parco del Lago. È aperto dalle 9. Porta la macchina fotografica!\"（提示：补充原因、你们会做什么、发出邀请。）",
             "limit": "50–80 词",
             "reference":
"""Cara Chiara,
domani vado al Parco Naturale del Lago con i miei genitori. Il parco è aperto dalle 9 alle 18 e ci sono bei sentieri per camminare e osservare gli uccelli. Porta la tua macchina fotografica! Non dimentichiamo di non lasciare rifiuti. Ci vediamo alle 8 alla stazione.
Un abbraccio,
Francesca"""},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力，权重 30%）",
         "items": [
            {"type": "mc", "prompt": "1. Cosa compra il cliente?", "options": ["borsa di tela", "bottiglia", "giornale"], "answer": 0},
            {"type": "mc", "prompt": "2. Quanto costa?", "options": ["1 euro", "2 euro", "3 euro"], "answer": 1},
            {"type": "mc", "prompt": "3. Con chi va al parco la ragazza?", "options": ["da sola", "col fratello", "con un amico"], "answer": 1},
            {"type": "mc", "prompt": "4. Cosa hanno fatto al parco?", "options": ["nuotato", "raccolto la spazzatura", "dormito"], "answer": 1},
            {"type": "mc", "prompt": "5. Quando è andata al parco?", "options": ["sabato", "domenica", "lunedì"], "answer": 1},
            {"type": "mc", "prompt": "6. Com'era il parco alla fine?", "options": ["più sporco", "più pulito", "chiuso"], "answer": 1},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语，10min）",
         "tasks": [
            {"desc":
"""① 自我介绍 + 习惯爱好；② 描述图片；③ 角色扮演。
任务：① 介绍自己并说一件减少塑料的小习惯；② 描述一张"自然公园"图片（树、湖、鸟）；③ 角色扮演：在游客中心向工作人员问公园门票与开放时间。""",
             "points": 30,
             "rubric":
"""① 自我介绍流畅、含习惯；② 图片描述用词准确（albero, lago, uccello）；③ 角色扮演完成信息询问；④ 语法基本正确、互动自然。""",
             "dims": [
                ("Pronuncia 发音", "发音清晰，重音基本正确"),
                ("Fluenza 流利度", "自我介绍流畅，含个人习惯"),
                ("Grammatica 语法", "现在时 / 近过去时使用基本正确"),
                ("Contenuto 内容", "涵盖自我介绍、图片描述、角色扮演三项任务"),
                ("Interazione 互动", "角色扮演用语得体，完成信息询问"),
             ],
             "ref":
"""Buongiorno, mi presento: mi chiamo Marco, ho ventidue anni e studio a Bologna. Per ridurre la plastica uso una borracchia di metallo e porto sempre la borsa di tela. Nella foto vedo un bel parco naturale: ci sono alberi verdi, un lago tranquillo e tanti uccelli che volano. È un posto molto bello e pulito. Scusi, un'informazione: quanto costa il biglietto del parco e a che ora chiude? Grazie mille!"""},
         ]},
    ],
})

# ============================== B1 =========================================
LEVELS.append({
    "code": "B1", "name": "CELI 2", "subtitle": "cambiamento climatico / energie rinnovabili",
    "theme": "🌱 Ambiente, clima e sostenibilità", "subj_max": 30,
    "audio": [
        {"title": "Notiziario — Il clima", "body":
"""Buongiorno. Oggi parliamo del clima. La scorsa estate è stata la più calda degli ultimi vent'anni. Alcune città hanno avuto problemi con l'acqua. Il comune ha deciso di piantare mille alberi lungo le strade per dare più ombra. Inoltre, metterà pannelli solari su tutti gli edifici pubblici entro il 2030."""},
        {"title": "Dialogo — Pannelli solari", "body":
"""Marco: Ho sentito che vuoi mettere i pannelli solari.
Anna: Sì! Così pago meno bollette e aiuto l'ambiente.
Marco: Quanto costa?
Anna: Circa 4000 euro, ma c'è un bonus del governo.
Marco: Ottima idea, lo farò anch'io."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，权重 25%）",
         "texts": [
            {"title": "Testo 1 — Articolo（气候变化短文）", "body":
"""Il cambiamento climatico è un problema grande. Negli ultimi anni le temperature sono aumentate. Molte estati sono molto calde e ci sono più temporali. Gli scienziati dicono che dobbiamo ridurre le emissioni di gas. Possiamo usare meno l'auto e risparmiare energia a casa."""},
            {"title": "Testo 2 — Avviso（公寓安装太阳能板通知）", "body":
"""Il nostro condominio installa pannelli solari sul tetto. L'energia del sole ci darà elettricità pulita. I lavori iniziano a marzo. Chi vuole informazioni può scrivere all'amministratore."""},
            {"title": "Testo 3 — Scheda（能源展信息）", "body":
"""Fiera dell'Energia Rinnovabile
Luogo: Centromostre        Data: 12 aprile
Orario: dalle 10 alle 19   Ingresso: ________ (gratis / 5 euro)
Parcheggio: ________ (disponibile / chiuso)"""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Secondo il testo, le temperature…", "options": ["sono diminuite", "sono aumentate", "non cambiano"], "answer": 1},
            {"type": "mc", "prompt": "2. Cosa suggeriscono gli scienziati?", "options": ["usare più l'auto", "ridurre le emissioni", "accendere il riscaldamento"], "answer": 1},
            {"type": "mc", "prompt": "3. Dove installano i pannelli solari?", "options": ["in giardino", "sul tetto", "in cantina"], "answer": 1},
            {"type": "mc", "prompt": "4. Quando iniziano i lavori?", "options": ["a gennaio", "a marzo", "ad aprile"], "answer": 1},
            {"type": "match", "prompt": "5. Associa: Testo 1 →", "options": ["cambiamento climatico", "energie rinnovabili"], "answer": 0},
            {"type": "match", "prompt": "   Testo 2 →", "options": ["cambiamento climatico", "energie rinnovabili"], "answer": 1},
            {"type": "match", "prompt": "   Testo 3 →", "options": ["cambiamento climatico", "energie rinnovabili"], "answer": 1},
            {"type": "cloze", "text": "6. Ingresso: ________", "answers": ["gratis"]},
            {"type": "cloze", "text": "7. Parcheggio: ________", "answers": ["disponibile"]},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 25%）",
         "tasks": [
            {"title": "Compito 1 — Questionario（能源习惯问卷，60–80 词）",
             "prompt": "Questionario \"La mia casa e l'energia\": 1. Usi lampadine a LED? 2. Quante volte a settimana usi l'auto? 3. Hai pannelli solari? 4. Un consiglio per risparmiare energia.",
             "limit": "60–80 词",
             "reference":
"""1. Sì, uso lampadine a LED perché consumano meno energia.
2. Uso l'auto tre volte a settimana, solo per andare al lavoro.
3. No, non abbiamo pannelli solari, ma mia zia li ha in campagna.
4. Un consiglio: spegnere le luci quando si esce e usare meno l'auto."""},
            {"title": "Compito 2 — E-mail（给朋友写邮件，120–150 词）",
             "prompt": "Scrivi una e-mail a un amico raccontando un'esperienza passata legata al clima / alle energie rinnovabili (es. una visita a un parco eolico o a pannelli solari, o un blackout che ti ha fatto riflettere).",
             "limit": "120–150 词",
             "reference":
"""Caro Paolo,
ti scrivo per raccontarti quello che è successo domenica scorsa. Siamo andati con la mia classe a visitare un parco eolico in collina. All'inizio non sapevo cosa aspettarmi, ma quando ho visto le grandi pale muoversi lentamente nel vento sono rimasto colpito. Una guida ci ha spiegato che il vento produce elettricità pulita per migliaia di famiglie. Poi siamo saliti in cima e il panorama era stupendo. Ho capito quanto sia importante investire in energie rinnovabili per il nostro futuro. Spero di tornarci presto con te!
Un abbraccio,
Luca"""},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力，权重 25%）",
         "items": [
            {"type": "mc", "prompt": "1. L'estate scorsa è stata…", "options": ["la più fredda", "la più calda", "normale"], "answer": 1},
            {"type": "mc", "prompt": "2. Quante alberi pianta il comune?", "options": ["cento", "mille", "diecimila"], "answer": 1},
            {"type": "mc", "prompt": "3. Entro quando i pannelli negli edifici pubblici?", "options": ["2025", "2030", "2035"], "answer": 1},
            {"type": "mc", "prompt": "4. Chi vuole mettere i pannelli solari?", "options": ["Marco", "Anna", "tutti e due"], "answer": 1},
            {"type": "mc", "prompt": "5. Quanto costano i pannelli?", "options": ["2000 €", "4000 €", "6000 €"], "answer": 1},
            {"type": "mc", "prompt": "6. C'è un bonus del governo?", "options": ["sì", "no"], "answer": 0},
            {"type": "mc", "prompt": "7. Cosa risparmia Anna?", "options": ["benzina", "bollette", "cibo"], "answer": 1},
            {"type": "mc", "prompt": "8. Marco farà la stessa cosa?", "options": ["sì", "no"], "answer": 0},
            {"type": "mc", "prompt": "9. (multi) Il problema dell'acqua è stato in…", "options": ["alcune città", "tutta Italia", "nessun posto"], "answer": 0},
            {"type": "mc", "prompt": "10. (multi) Gli edifici pubblici avranno pannelli…", "options": ["entro il 2030", "mai", "già ora"], "answer": 0},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语，权重 25%）",
         "tasks": [
            {"desc":
"""① 自我介绍 / 兴趣 / 日常；② 描述图片；③ 角色扮演。
任务：① 介绍自己对气候变化的看法与日常节能习惯；② 描述一张"太阳能板 / 风车"图片；③ 角色扮演：向邻居解释为什么要减少开车、改用可再生能源。""",
             "points": 30,
             "rubric":
"""① 连贯自我介绍与观点；② 图片描述准确（pannello solare / pala eolica）；③ 角色扮演说服力强、用语得体；④ 语法（现在时 / 近过去时）较准确、互动顺畅。""",
             "dims": [
                ("Pronuncia 发音", "发音标准，语调节奏自然"),
                ("Fluenza 流利度", "连贯表达观点与习惯，少停顿"),
                ("Grammatica 语法", "现在时 / 近过去时较准确，尝试复合句"),
                ("Contenuto 内容", "观点明确，图片描述准确（pannello solare / pala eolica）"),
                ("Interazione 互动", "说服性角色扮演，用语得体"),
             ],
             "ref":
"""Secondo me il cambiamento climatico è il problema più importante di oggi. A casa risparmio energia: spengo le luci, uso meno l'auto e riciclo sempre. Nella foto ci sono dei pannelli solari sul tetto e una pala eolica in campagna: sono fonti rinnovabili e pulite. Senti, vicino: perché non lasci la macchina ogni tanto? Con il solare e l'eolico risparmiamo e aiutiamo il clima. Che ne dici di provare insieme?"""},
         ]},
    ],
})

# ============================== B2 =========================================
LEVELS.append({
    "code": "B2", "name": "CELI 3", "subtitle": "economia circolare / mobilità sostenibile",
    "theme": "🌱 Ambiente, clima e sostenibilità", "subj_max": 50,
    "audio": [
        {"title": "Intervista — Economia circolare", "body":
"""Giornalista: Professore, cos'è l'economia circolare?
Esperto: È un sistema dove niente si spreca. Si ripara, si riusa, si ricicla.
Giornalista: Funziona per le piccole imprese?
Esperto: Sì, ma serve formazione. Chi impara, risparmia e crea lavoro.
Giornalista: E i cittadini?
Esperto: Possono comprare usato e condividere oggetti con i vicini."""},
        {"title": "Servizio — Bike sharing", "body":
"""La nostra città ha aperto 20 nuove stazioni di bike sharing. Ogni giorno 5.000 persone lasciano l'auto a casa. Il sindaco dice: "Vogliamo 50 stazioni entro il 2026". Così l'aria sarà più pulita e il traffico calerà."""},
        {"title": "Monologo — Piano della mobilità", "body":
"""Il Comune ha presentato il nuovo piano della mobilità. Ci saranno più piste ciclabili e meno parcheggi in centro. Il trasporto pubblico sarà gratis la domenica. L'obiettivo è ridurre il traffico del 30% in cinque anni. I cittadini possono inviare commenti sul sito entro giugno."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，A.1+A.2+A.3）",
         "texts": [
            {"title": "A.1 — Testo 1", "body":
"""L'economia circolare rappresenta un cambiamento di paradigma rispetto al modello lineare "estrai-produci-getta". In un sistema circolare, i materiali restano in circolo il più a lungo possibile attraverso riparazione, riutilizzo e riciclo. Le aziende che adottano questo modello non solo riducono i rifiuti, ma ottengono spesso anche vantaggi economici grazie a una maggiore efficienza. Tuttavia, la transizione richiede investimenti iniziali e un cambiamento culturale profondo da parte di consumatori e imprese."""},
            {"title": "A.1 — Testo 2", "body":
"""Alcuni esempi concreti di economia circolare includono il deposito su cauzione per le bottiglie, la condivisione di attrezzature tra vicini e la rigenerazione di edifici invece della loro demolizione. Secondo uno studio europeo, applicare i principi dell'economia circolare potrebbe creare oltre 700.000 posti di lavoro entro il 2030. La sfida resta quella di rendere questi modelli scalabili e accessibili anche alle piccole imprese, che oggi faticano a sostenere i costi di avvio."""},
            {"title": "A.2 — Testo A（mobilità sostenibile I）", "body":
"""La mobilità sostenibile punta a ridurre l'uso dell'auto privata. Sempre più città italiane ampliano le piste ciclabili e i servizi di bike sharing. A Milano il sistema BikeMi conta migliaia di utenti giornalieri, mentre a Bologna il tram torna a essere centrale."""},
            {"title": "A.2 — Testo B（mobilità sostenibile II）", "body":
"""Il car sharing permette di usare un'auto solo quando serve, abbassando il numero di veicoli in circolazione. Nel frattempo, i bus elettrici entrano nei centri storici e migliorano la qualità dell'aria. Alcuni comuni incentivano anche il telelavoro per ridurre gli spostamenti."""},
            {"title": "A.3 — Testo（mobilità e urbanistica）", "body":
"""La transizione verso una mobilità a basse emissioni non riguarda solo i mezzi di trasporto, ma anche la pianificazione urbana. Se le persone vivono lontano dal lavoro e dai servizi, nessun bus elettrico potrà da solo risolvere il problema. Serve una visione integrata che unisca trasporto pubblico, ciclabilità e prossimità dei servizi. Alcune amministrazioni sperimentano le "zone 30", dove il limite è di 30 km/h, rendendo le strade più sicure e vivibili."""},
         ],
         "items": [
            {"type": "mc", "prompt": "A.1-1. Il modello lineare è definito come…", "options": ["ripara e riusa", "estrai-produci-getta", "ricicla tutto", "consuma meno"], "answer": 1},
            {"type": "mc", "prompt": "A.1-2. Nell'economia circolare i materiali…", "options": ["si buttano subito", "restano in circolo", "si bruciano", "si nascondono"], "answer": 1},
            {"type": "mc", "prompt": "A.1-3. Le aziende circolari ottengono…", "options": ["solo costi", "vantaggi economici", "multe", "nessun cambiamento"], "answer": 1},
            {"type": "mc", "prompt": "A.1-4. La transizione richiede…", "options": ["solo tempo", "investimenti e cambiamento culturale", "niente", "solo leggi"], "answer": 1},
            {"type": "mc", "prompt": "A.1-5. Esempio concreto NON citato:", "options": ["cauzione bottiglie", "sharing attrezzature", "demolizione sistematica", "rigenerazione edifici"], "answer": 2},
            {"type": "mc", "prompt": "A.1-6. Posti di lavoro entro 2030:", "options": ["70.000", "700.000", "7 milioni", "nessuno"], "answer": 1},
            {"type": "mc", "prompt": "A.1-7. La sfida principale è…", "options": ["troppa domanda", "scalabilità per piccole imprese", "troppi rifiuti", "poca acqua"], "answer": 1},
            {"type": "mc", "prompt": "A.1-8. «Scalabili» significa…", "options": ["distruttibili", "ampliabili", "costosi", "piccoli"], "answer": 1},
            {"type": "mc", "prompt": "A.1-9. Il tono del testo è…", "options": ["pubblicitario", "informativo/analitico", "comico", "nostalgico"], "answer": 1},
            {"type": "match", "prompt": "A.2-1. Ampliamento delle piste ciclabili →", "options": ["A", "B", "A+B"], "answer": 0},
            {"type": "match", "prompt": "A.2-2. Il car sharing riduce i veicoli →", "options": ["A", "B", "A+B"], "answer": 1},
            {"type": "match", "prompt": "A.2-3. I bus elettrici migliorano l'aria →", "options": ["A", "B", "A+B"], "answer": 1},
            {"type": "match", "prompt": "A.2-4. BikeMi a Milano →", "options": ["A", "B", "A+B"], "answer": 0},
            {"type": "match", "prompt": "A.2-5. Il tram a Bologna →", "options": ["A", "B", "A+B"], "answer": 0},
            {"type": "match", "prompt": "A.2-6. Incentivi al telelavoro →", "options": ["A", "B", "A+B"], "answer": 1},
            {"type": "match", "prompt": "A.2-7. Obiettivo: meno auto privata →", "options": ["A", "B", "A+B"], "answer": 2},
            {"type": "match", "prompt": "A.2-8. Qualità dell'aria nei centri storici →", "options": ["A", "B", "A+B"], "answer": 1},
            {"type": "match", "prompt": "A.2-9. Condivisione dell'auto →", "options": ["A", "B", "A+B"], "answer": 1},
            {"type": "match", "prompt": "A.2-10. Utenti giornalieri a migliaia →", "options": ["A", "B", "A+B"], "answer": 0},
            {"type": "open", "prompt": "A.3-1. Perché un bus elettrico non basta da solo?", "ref": "Perché le persone vivono lontano da lavoro/servizi.", "rows": 2},
            {"type": "open", "prompt": "A.3-2. Cosa significa \"prossimità dei servizi\"?", "ref": "Avere servizi vicino a casa.", "rows": 2},
            {"type": "open", "prompt": "A.3-3. Cosa sono le \"zone 30\" e che effetto hanno?", "ref": "Zone con limite 30 km/h, più sicure e vivibili.", "rows": 2},
            {"type": "open", "prompt": "A.3-4. Qual è il messaggio centrale del testo?", "ref": "Serve pianificazione urbana integrata, non solo mezzi puliti.", "rows": 2},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 20%）",
         "tasks": [
            {"title": "B.1 — Saggio breve（二选一，120–180 词）",
             "prompt": "a) Racconta un'esperienza personale legata all'economia circolare (es. riparare invece di comprare, mercatino dell'usato). b) Descrivi come la tua città potrebbe migliorare la mobilità sostenibile.",
             "limit": "120–180 词",
             "reference":
"""L'anno scorso ho deciso di provare l'economia circolare nella vita di tutti i giorni. Invece di comprare sempre oggetti nuovi, ho iniziato a riparare le mie scarpe da ginnastica e a frequentare un mercatino dell'usato nel mio quartiere. Una volta ho trovato una bicicletta quasi nuova a pochi euro: l'ho sistemata con l'aiuto di un vicino e da allora la uso per andare al lavoro. Questa scelta mi ha fatto risparmiare denaro e, soprattutto, mi ha fatto sentire utile per l'ambiente. Credo che condividere e riusare sia molto più intelligente che gettare via. Se più persone facessero così, produrremmo molti meno rifiuti e vivremmo in una città più pulita."""},
            {"title": "B.2 — E-mail / lettera（三选一，80–100 词）",
             "prompt": "a) Scrivi al comune per chiedere informazioni su un nuovo servizio di bike sharing. b) Scrivi a un amico per consigliargli di usare meno la plastica. c) Scrivi all'amministratore del condominio per proporre pannelli solari sul tetto.",
             "limit": "80–100 词",
             "reference":
"""Gentile Ufficio Mobilità,
sono un cittadino interessato al nuovo servizio di bike sharing della nostra città. Vorrei sapere quante stazioni saranno attive e a quanto ammonterà il costo dell'abbonamento mensile. Inoltre, è previsto un sistema di prenotazione tramite applicazione? Resto in attesa di un cortese riscontro e la ringrazio per l'attenzione.
Cordiali saluti,
Marco Rossi"""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力，权重 10%）",
         "cloze": {"cloze_text":
"""L'economia circolare è un modello _____ (1) riduce gli sprechi e permette _____ (2) riutilizzare i materiali più volte. Invece _____ (3) gettare tutto, le aziende riparano e riciclano. Questo sistema richiede meno risorse nuove e aiuta _____ (4) ambiente a rimanere pulito. Molti consumatori vi partecipano attivamente, perché _____ (5) traggono beneficio a lungo termine. È importante cambiare abitudini e scegliere prodotti _____ (6) durano di più. Noi _____ (7) dobbiamo sostenere con politiche chiare. In _____ (8) modo si crea molto meno rifiuto. Le famiglie _____ (9) adottano risparmiano ogni mese. Tale approccio porta _____ (10) risultati concreti. _____ (11) città più virtuose ottengono incentivi statali. _____ (12) tutto ciò dimostra che il cambiamento è possibile.

La mobilità sostenibile _____ (13) diventata una priorità per le città italiane. Sempre più persone vanno _____ (14) lavoro in bicicletta oppure _____ (15) autobus elettrici. I comuni investono _____ (16) piste ciclabili e _____ (17) cittadini le usano volentieri. Per ridurre il traffico serve anche il car sharing, _____ (18) permette di condividere l'auto quando _____ (19) serve. Chi abita lontano _____ (20) centro può contare sui treni regionali. _____ (21) futuro dipende dalle nostre scelte quotidiane, perciò dobbiamo agire _____ (22) fretta. _____ (23) noi dipende il benessere del pianeta.""",
            "answers": ["che","di","di","l'","ne","che","lo","questo","che","a","Le","Tutto","è","al","con","in","i","che","ne","dal","Il","con","Da"]},
         "rewrite": [
            {"prompt": "1. Le città piantano alberi. Gli alberi offrono ombra. Così il clima è più fresco. → con «in modo che»", "ref": "Le città piantano alberi in modo che offrano ombra e il clima sia più fresco."},
            {"prompt": "2. Abbiamo ridotto i rifiuti. Abbiamo risparmiato denaro. Inoltre abbiamo aiutato l'ambiente. → con «non solo… ma anche»", "ref": "Non solo abbiamo ridotto i rifiuti e risparmiato denaro, ma abbiamo anche aiutato l'ambiente."},
            {"prompt": "3. Usi la bici. Eviti il traffico. Risparmi benzina. → con «così che»", "ref": "Usi la bici così che eviti il traffico e risparmi benzina."},
            {"prompt": "4. Il Comune ha aperto le stazioni. Le stazioni sono vicine alla scuola. I ragazzi le usano. → con «che / le quali»", "ref": "Il Comune ha aperto le stazioni che sono vicine alla scuola e che i ragazzi usano."},
            {"prompt": "5. Piove forte. Non usciamo. Restiamo a casa. → con «poiché»", "ref": "Poiché piove forte, non usciamo e restiamo a casa."},
            {"prompt": "6. Ricicli la carta. Compri meno prodotti nuovi. Produci meno CO2. → con «se»", "ref": "Se ricicli la carta e compri meno prodotti nuovi, produci meno CO2."},
            {"prompt": "7. Le energie rinnovabili costano meno. Le energie rinnovabili inquinano meno. Convengono a tutti. → con «in quanto»", "ref": "Le energie rinnovabili convengono a tutti, in quanto costano meno e inquinano meno."},
         ],
         "wordform": [
            {"text": "1. Noi _____ (riciclare) la carta ogni settimana.", "answers": ["ricicliamo"]},
            {"text": "2. L'uso _____ (eccessivo) della plastica fa male.", "answers": ["eccessivo"]},
            {"text": "3. È _____ (importante) risparmiare energia.", "answers": ["importante"]},
            {"text": "4. Hanno _____ (installare) i pannelli sul tetto.", "answers": ["installato"]},
            {"text": "5. La città è _____ (pulito) quest'anno.", "answers": ["pulita"]},
            {"text": "6. Parliamo di un problema _____ (ambiente).", "answers": ["ambientale"]},
            {"text": "7. Dobbiamo _____ (andare) in bici al lavoro.", "answers": ["andare"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力，权重 20%）",
         "items": [
            {"type": "mc", "prompt": "D.1-1. L'economia circolare…", "options": ["spreca", "ripara e riusa", "brucia", "compra"], "answer": 1},
            {"type": "mc", "prompt": "D.1-2. Serve…", "options": ["soldi soltanto", "formazione", "automobili", "benzina"], "answer": 1},
            {"type": "mc", "prompt": "D.1-3. I cittadini possono…", "options": ["comprare usato", "ignorare", "pagare", "viaggiare"], "answer": 0},
            {"type": "mc", "prompt": "D.1-4. Nuove stazioni bike sharing:", "options": ["2", "20", "200", "0"], "answer": 1},
            {"type": "mc", "prompt": "D.1-5. Persone che lasciano l'auto:", "options": ["500", "5.000", "50.000", "500.000"], "answer": 1},
            {"type": "mc", "prompt": "D.1-6. Obiettivo stazioni entro 2026:", "options": ["10", "50", "100", "5"], "answer": 1},
            {"type": "mc", "prompt": "D.1-7. Risultato atteso:", "options": ["più traffico", "aria più pulita", "più auto", "nulla"], "answer": 1},
            {"type": "mc", "prompt": "D.1-8. Il piano è presentato da…", "options": ["un giornale", "il Comune", "una scuola", "un'azienda"], "answer": 1},
            {"type": "mc", "prompt": "D.1-9. Trasporto gratis la…", "options": ["domenica", "lunedì", "sera", "notte"], "answer": 0},
            {"type": "mc", "prompt": "D.1-10. Ridurre il traffico del…", "options": ["3%", "30%", "300%", "0%"], "answer": 1},
            {"type": "cloze", "text": "D.2-1. Il Comune presenta il nuovo piano della ________.", "answers": ["mobilità"]},
            {"type": "cloze", "text": "D.2-2. Ci saranno più piste ________.", "answers": ["ciclabili"]},
            {"type": "cloze", "text": "D.2-3. Meno ________ in centro.", "answers": ["parcheggi"]},
            {"type": "cloze", "text": "D.2-4. Trasporto pubblico gratis la ________.", "answers": ["domenica"]},
            {"type": "cloze", "text": "D.2-5. Obiettivo: ridurre il traffico del ________% in 5 anni.", "answers": ["30"]},
            {"type": "cloze", "text": "D.2-6. I cittadini inviano ________ sul sito.", "answers": ["commenti"]},
            {"type": "cloze", "text": "D.2-7. Termine per i commenti: ________.", "answers": ["giugno"]},
            {"type": "cloze", "text": "D.2-8. L'idea è migliorare la ________.", "answers": ["qualità"]},
            {"type": "cloze", "text": "D.2-9. Meno auto significa meno ________.", "answers": ["inquinamento"]},
            {"type": "cloze", "text": "D.2-10. Il piano dura ________ anni.", "answers": ["cinque"]},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语，权重 30%）",
         "tasks": [
            {"desc":
"""① 描述图片并回答；② 概述短文并回答；③ 情境角色扮演。
任务：① 描述一张"垃圾分类 / 循环经济"信息图并回答考官追问；② 用 2–3 句概述一段关于"共享汽车"的短文并评论；③ 角色扮演：你是一位市民，在听证会上向市长提议扩宽自行车道。""",
             "points": 50,
             "rubric":
"""① 图片描述准确、语域恰当；② 概述完整、评论有个人立场；③ 角色扮演逻辑清晰、说服力强；④ 语法（虚拟 / 条件 / 关系代词）较准确；⑤ 流利度与互动。""",
             "dims": [
                ("Pronuncia 发音", "发音标准，语域与场合匹配"),
                ("Fluenza 流利度", "表达连贯，能展开论述与评论"),
                ("Grammatica 语法", "虚拟 / 条件 / 关系代词较准确"),
                ("Contenuto 内容", "概述完整、立场清晰，论证有逻辑"),
                ("Interazione 互动", "听证会角色扮演说服力强"),
             ],
             "ref":
"""L'infografica mostra come separare i rifiuti: carta, plastica, vetro e umido. Ogni materiale diventa una nuova risorsa, ed è questo il cuore dell'economia circolare. Il testo sul car sharing dice che condividere l'auto riduce il numero di veicoli in circolazione e migliora l'aria. Sono d'accordo, però servono anche piste ciclabili sicure. Signor Sindaco, propongo di ampliare le ciclabili in centro: meno traffico significa una città più sana e vivibile per tutti i cittadini."""},
         ]},
    ],
})

# ============================== C1 =========================================
LEVELS.append({
    "code": "C1", "name": "CELI 4", "subtitle": "politiche ambientali europee / decrescita",
    "theme": "🌱 Ambiente, clima e sostenibilità", "subj_max": 50,
    "audio": [
        {"title": "Intervista — Green Deal e decrescita", "body":
"""Conduttrice: Oggi con la dottoressa Bianchi parliamo del Green Deal.
Bianchi: Il fondo per la transizione aiuta le regioni più colpite. Tuttavia, servono tempi certi.
Conduttrice: I cittadini cosa devono fare?
Bianchi: Isolate le case, usate meno auto, ma soprattutto votate politiche coerenti.
Conduttrice: La decrescita è realistica?
Bianchi: È un ideale utile al dibattito, ma servono passi concreti entro il 2030."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，权重 20%）",
         "texts": [
            {"title": "Testo A — Politiche ambientali europee（欧盟绿色协议）", "body":
"""Il Green Deal europeo ambisce a rendere l'Unione climaticamente neutra entro il 2050. Prevede il riassetto profondo di industria, agricoltura e trasporti attraverso incentivi e normative vincolanti. Sebbene molti Stati membri ne condividano la visione, la transizione solleva tensioni: i costi ricadono in modo disuguale sui cittadini a basso reddito, alimentando il dibattito sulla "giustizia climatica". La Commissione risponde con fondi di compensazione, ma l'efficacia resta oggetto di valutazione."""},
            {"title": "Testo B — Decrescita（去增长批判）", "body":
"""I sostenitori della decrescita osservano che la crescita infinita su un pianeta finito è un'illusione. Propongono di ridurre la produzione e il consumo per rientrare nei limiti ecologici, privilegiando il benessere sul Pil. I critici replicano che senza crescita non si finanziano sanità e istruzione. La posizione intermedia suggerisce una "decrescita selettiva": meno merci inutili, più servizi sociali. Il confronto resta acceso e poco tradotto in policy concrete."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. L'obiettivo del Green Deal è…", "options": ["crescita illimitata", "neutralità climatica 2050", "abolire l'industria", "tagliare i fondi"], "answer": 1},
            {"type": "mc", "prompt": "2. La \"giustizia climatica\" riguarda…", "options": ["solo le imprese", "la distribuzione disuguale dei costi", "il clima spaziale", "le tasse doganali"], "answer": 1},
            {"type": "mc", "prompt": "3. La decrescita privilegia…", "options": ["il Pil", "il benessere", "la produzione massima", "il debito"], "answer": 1},
            {"type": "mc", "prompt": "4. I critici della decrescita temono…", "options": ["troppa natura", "meno risorse per sanità/istruzione", "troppe tasse", "il freddo"], "answer": 1},
            {"type": "tf", "prompt": "5. La Commissione offre fondi di compensazione. (V/F)", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "6. La decrescita è già ampiamente tradotta in leggi. (V/F)", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "7. Entrambi i testi parlano di tensioni tra economia e ambiente. (V/F)", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "8. Il Green Deal usa solo strumenti volontari. (V/F)", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "mc", "prompt": "9. (analitica) Quale tono predomina nel Testo B?", "options": ["informativo", "polemico", "neutrale-analitico"], "answer": 2},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 30%）",
         "tasks": [
            {"title": "Compito — Riassunto（摘要，max 50–60 词）",
             "prompt": "Scrivi un riassunto del seguente testo: \"Le politiche ambientali europee puntano alla neutralità climatica, ma incontrano resistenze per i costi sociali. La decrescita propone un modello alternativo basato sul benessere più che sulla crescita, pur rimanendo controverso. Serve un dialogo tra approcci per una transizione giusta.\"",
             "limit": "50–60 词",
             "reference":
"""Le politiche europee mirano alla neutralità climatica ma incontrano resistenze per i costi sociali. La decrescita offre un modello alternativo fondato sul benessere anziché sulla crescita, benché controversa. È necessario un dialogo tra approcci per realizzare una transizione giusta ed efficace."""},
            {"title": "Compito — Saggio / articolo（议论文，200–250 词）",
             "prompt": "Scrivi un articolo/saggio a favore o contro le politiche ambientali europee, integrando il tema della decrescita (200–250 parole).",
             "limit": "200–250 词",
             "reference":
"""A favore di una politica ambientale europea ambiziosa
Credo che il Green Deal europeo rappresenti una risposta necessaria alla crisi climatica, purché venga accompagnato da strumenti di equità sociale. La neutralità al 2050 non è un lusso, ma una condizione di sopravvivenza: senza interventi strutturali, i costi ambientali ricadranno proprio sui più vulnerabili. Tuttavia, condivido i critici della decrescita quando osservano che ridurre la produzione senza proteggere welfare rischia di creare nuove povertà. La soluzione, a mio parere, sta in una "decrescita selettiva": meno merci inutili e più servizi pubblici. L'Europa deve dunque combinare norme vincolanti con fondi di compensazione ben distribuiti. Solo così la transizione sarà accettata dai cittadini e davvero sostenibile nel lungo periodo."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力，权重 10%）",
         "cloze": {"cloze_text":
"""Il Green Deal europeo ambisce a rendere l'Unione climaticamente neutra entro il 2050, _____ (1) obiettivo richiede un riassetto profondo dell'industria. Sebbene molti Stati _____ (2) condividano la visione, la transizione solleva tensioni sociali, _____ (3) i costi ricadono in modo disuguale sui cittadini a basso reddito. La Commissione risponde _____ (4) fondi di compensazione, _____ (5) devono essere bene distribuiti. È necessario che tali risorse _____ (6) (essere) impiegate in modo efficiente. I critici osservano che, _____ (7) la crescita continuasse senza limiti, il pianeta non reggerebbe. Per questo alcuni propongono la decrescita, _____ (8) obiettivo è ridurre la produzione. Tale modello, _____ (9) (considerare) controverso, privilegia il benessere sul Pil. La posizione intermedia suggerisce una decrescita selettiva, _____ (10) meno merci inutili e più servizi sociali. _____ (11) confronto resta acceso e poco tradotto in policy concrete. Serve un dialogo _____ (12) gli approcci per una transizione giusta. _____ (13) le imprese non collaborano, gli obiettivi falliranno. È auspicabile che i governi _____ (14) (adottare) norme vincolanti entro il 2030. Chi inquina _____ (15) (dovere) pagare di più. _____ (16) ridurre le emissioni serve anche cambiare stili di vita, _____ (17) richiede l'impegno quotidiano dei cittadini. I fondi europei _____ (18) (destinare) alle regioni più colpite. Nonostante le difficoltà, _____ (19) (credere) che la transizione sia possibile. _____ (20) tale sforzo dipende la credibilità dell'Europa. _____ (21) cittadini chiedono chiarezza e coerenza. _____ (22) tutto ciò, la giustizia climatica resta un traguardo lontano. _____ (23) realizzarlo occorrono passi concreti.""",
            "answers": ["il cui","lo","perché","con","che","siano","se","il cui","considerato","con","Il","tra","Se","adottino","deve","Per","il che","sono destinati","credo","Da","I","Nonostante","Per"]},
         "rewrite": [
            {"prompt": "1. Trasforma in forma passiva: «L'Unione ha fissato l'obiettivo della neutralità.»", "ref": "L'obiettivo della neutralità è stato fissato dall'Unione."},
            {"prompt": "2. Riscrivi con il congiuntivo: «È necessario. Il Parlamento approva la legge.»", "ref": "È necessario che il Parlamento approvi la legge."},
            {"prompt": "3. Unisci con un pronome relativo: «La decrescita riduce la produzione. Molti giovani la sostengono.»", "ref": "La decrescita, che molti giovani sostengono, riduce la produzione."},
            {"prompt": "4. Trasforma con il condizionale: «Se adottiamo misure severe, l'aria migliora.»", "ref": "Se adottassimo misure severe, l'aria migliorerebbe."},
            {"prompt": "5. Riscrivi con «nonostante»: «Piove. Noi usciamo in bici.»", "ref": "Nonostante piova, noi usciamo in bici."},
            {"prompt": "6. Trasforma in forma passiva: «I cittadini devono cambiare stili di vita.»", "ref": "Gli stili di vita devono essere cambiati dai cittadini."},
            {"prompt": "7. Riscrivi con «a meno che»: «Cambiamo subito. Perdiamo la credibilità.»", "ref": "A meno che non cambiamo subito, perderemo la credibilità."},
         ],
         "wordform": [
            {"text": "1. È indispensabile che il governo _____ (approvare) norme vincolanti.", "answers": ["approvi"]},
            {"text": "2. Se avessimo agito prima, oggi _____ (esserci) meno inquinamento.", "answers": ["ci sarebbe"]},
            {"text": "3. La tassa _____ (introdurre) nel 2023 ha ridotto le emissioni.", "answers": ["introdotta"]},
            {"text": "4. Chi _____ (violare) le norme sarà sanzionato.", "answers": ["viola"]},
            {"text": "5. Contribuire alla sostenibilità _____ (significare) cambiare abitudini.", "answers": ["significa"]},
            {"text": "6. Senza il vostro impegno, nulla _____ (potere) cambiare.", "answers": ["potrebbe"]},
            {"text": "7. Perché la transizione _____ (essere) giusta, servono fondi di compensazione.", "answers": ["sia"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力，权重 15%）",
         "items": [
            {"type": "cloze", "text": "Tabella 1. Fondo transizione: aiuta le regioni ________.", "answers": ["più colpite"]},
            {"type": "cloze", "text": "Tabella 2. Azione cittadini 1: isolate le ________.", "answers": ["case"]},
            {"type": "cloze", "text": "Tabella 3. Azione cittadini 2: usate meno ________.", "answers": ["auto"]},
            {"type": "cloze", "text": "Tabella 4. Orizzonte concreto: entro il ________.", "answers": ["2030"]},
            {"type": "tf", "prompt": "V/F 1. Il fondo aiuta solo le grandi imprese.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "V/F 2. La decrescita è presentata come ideale di dibattito.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "V/F 3. Servono passi concreti entro il 2030.", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语，权重 25%）",
         "tasks": [
            {"desc":
"""带材料面试（长篇论述 + 深度讨论）。
Materiale：Un breve articolo sul Green Deal e uno sulla decrescita。
Task：① 用 2–3 分钟阐述你对"欧洲环境政策 vs 去增长"的立场；② 考官追问（es. "Come finanziamo la transizione senza penalizzare i poveri?"），进行深度讨论。""",
             "points": 50,
             "rubric":
"""① 论述结构清晰、语域正式；② 准确使用虚拟 / 条件 / 被动；③ 立场明确并回应质疑；④ 词汇丰富（neutralità, equità, vincolante）；⑤ 互动与连贯。""",
             "dims": [
                ("Pronuncia 发音", "发音精准，语调节奏自如"),
                ("Fluenza 流利度", "长篇论述流畅，衔接自然"),
                ("Grammatica 语法", "虚拟 / 条件 / 被动准确，句式丰富"),
                ("Contenuto 内容", "立场明确，词汇丰富（neutralità, equità, vincolante）"),
                ("Interazione 互动", "深度讨论中回应质疑，逻辑自洽"),
             ],
             "ref":
"""La mia posizione è che le politiche ambientali europee e la decrescita non si escludono, ma vanno calibrate con attenzione. Il Green Deal europeo ambisce alla neutralità climatica entro il 2050 e, a mio parere, è un obiettivo giusto e necessario: nessuna economia può crescere a lungo su un pianeta in esaurimento. Tuttavia la transizione ha un costo, e questo costo ricade in modo disuguale sui cittadini a basso reddito. È qui che entra la giustizia climatica: se le misure sono vincolanti ma non eque, rischiamo di alienare proprio chi dovrebbe sostenere il cambiamento.

La decrescita selettiva mi convince proprio perché non chiede di fermare tutto, ma di ridurre ciò che è inutile — meno merci, più servizi sociali — per rientrare nei limiti ecologici. Non rinunciamo alla crescita della cura, ma a una crescita distruttiva.

E come finanziamo la transizione senza penalizzare i poveri? Userei i fondi di compensazione europei e una fiscalità ecologica progressiva, in cui chi inquina di più paga di più e il ricavato sostiene le famiglie. Insomma, servono sia norme vincolanti sia strumenti equi: la sostenibilità sarà realtà solo se sarà anche giusta."""},
         ]},
    ],
})

# ============================== C2 =========================================
LEVELS.append({
    "code": "C2", "name": "CELI 5", "subtitle": "antropocene / etica del rapporto uomo-natura",
    "theme": "🌱 Ambiente, clima e sostenibilità", "subj_max": 50,
    "audio": [
        {"title": "Dibattito — Antropocene ed etica", "body":
"""Relatore: L'Antropocene non è una scoperta, è una resa di conti. Abbiamo trattato il pianeta come un magazzino infinito, e ora la fattura arriva. Chi invoca il dominio della natura confonde il potere con la saggezza. La vera etica non chiede di tornare indietro, ma di abitare con misura. L'audience deve capire: non siamo padroni, siamo ospiti provvisori."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，权重 20%）",
         "texts": [
            {"title": "Testo — Saggio sull'Antropocene", "body":
"""Non viviamo più in un mondo che ci ospita; abitiamo una costruzione della quale siamo, insieme, architetti e detriti. L'Antropocene — questa etichetta geologica che suona come un epitaffio — segna il momento in cui l'umanità è diventata forza tellurica, capace di riplasmare atmosfere e fondali. E tuttavia, proprio mentre celebrano il trionfo della tecnica, le nostre società scoprono di essere ostaggi del proprio successo. L'etica del rapporto uomo-natura non può più essere un accessorio della coscienza: è la grammatica stessa della sopravvivenza. Negare tale dipendenza è la forma più raffinata di antropocentrismo, quello che confonde il dominio con la libertà."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. (dettaglio) L'Antropocene è definito come…", "options": ["un'era glaciale", "il momento in cui l'uomo è forza tellurica", "una religione", "un errore"], "answer": 1},
            {"type": "mc", "prompt": "2. (metafora) «architetti e detriti» suggerisce che l'uomo è…", "options": ["solo creatore", "creatore e rifiuto di ciò che crea", "innocente", "antico"], "answer": 1},
            {"type": "mc", "prompt": "3. (ironia/tono) «epitaffio» e «trionfo della tecnica» rivelano un tono…", "options": ["celebrativo", "ironico e ammonitore", "comico", "ingenuo"], "answer": 1},
            {"type": "mc", "prompt": "4. (posizione autore) L'autore ritiene l'antropocentrismo…", "options": ["una liberazione", "un errore che confonde dominio e libertà", "una soluzione", "irrilevante"], "answer": 1},
            {"type": "mc", "prompt": "5. (inferenza) «grammatica della sopravvivenza» significa che l'etica è…", "options": ["ornamentale", "strutturale e necessaria", "superflua", "opzionale"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 30%）",
         "tasks": [
            {"title": "Compito 1 — Saggio / articolo（二选一，约 250 词）",
             "prompt": "a) \"L'Antropocene ci obbliga a ripensare l'etica del rapporto uomo-natura\": sviluppa una tesi argomentata. b) Redigi un \"policy brief\" per un ente pubblico: tre raccomandazioni etiche per le politiche ambientali.",
             "limit": "约 250 词",
             "reference":
"""L'Antropocene ci obbliga a ripensare l'etica del rapporto uomo-natura
L'ingresso nell'Antropocene segna la fine di un'illusione: quella di un mondo esterno, silente e disponibile, su cui l'umano potesse esercitare un dominio senza conseguenze. Oggi sappiamo che non abitiamo la natura dal di fuori, ma ne siamo tessuto. Questa consapevolezza impone un ribaltamento etico: non più padroni, ma custodi provvisori. Un'etica rinnovata deve innanzitutto riconoscere i limiti planetari come vincolo, non come ostacolo allo sviluppo. In secondo luogo, deve ampliare la comunità morale oltre l'umano, includendo ecosistemi e generazioni future cui non possiamo parlare, ma cui dobbiamo giustizia. Infine, richiede coerenza tra sapere e agire: denunciare il disastro senza mutare stili di vita è la forma più seducente di ipocrisia. La sostenibilità, dunque, non è tecnica applicata all'etica, ma etica divenuta condizione della tecnica. Solo accettando la nostra fragilità potremo abitare con misura il pianeta che ci ospita."""},
            {"title": "Compito 2 — Seconda prova（评论，80–100 词）",
             "prompt": "Scrivi una breve recensione critica del testo in lettura, giudicandone efficacia retorica e posizione etica.",
             "limit": "80–100 词",
             "reference":
"""Il saggio in lettura colpisce per la densità metaforica: "architetti e detriti" riduce in immagine la contraddizione dell'umano contemporaneo. Il tono, tra ironia e ammonimento, evita il facile catastrofismo e costruisce invece un argomento fermo: l'antropocentrismo confonde dominio e libertà. La posizione etica — l'etica come grammatica della sopravvivenza — è convincente, benché il testo resti sul piano filosofico e poco tradotto in policy. Nel complesso, un testo retoricamente efficace e provocatorio."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力，权重 10%）",
         "cloze": {"cloze_text":
"""Non viviamo più in un mondo che _____ (1) ospita; abitiamo una costruzione della _____ (2) siamo, insieme, architetti e detriti. L'Antropocene — etichetta _____ (3) suona come un epitaffio — segna il momento in cui l'umanità è diventata forza tellurica, capace _____ (4) riplasmare atmosfere e fondali. E tuttavia, proprio _____ (5) celebrano il trionfo della tecnica, le nostre società scoprono di essere ostaggi del proprio successo. L'etica del rapporto uomo-natura non può più essere un accessorio della coscienza: è la grammatica _____ (6) della sopravvivenza. Negare tale dipendenza è la forma _____ (7) raffinata di antropocentrismo, _____ (8) confonde il dominio con la libertà. _____ (9) l'umanità non ripensi tale rapporto, il pianeta continuerà a soffrire. È auspicabile che ciascuno _____ (10) (riconoscere) i propri limiti planetari. Chi _____ (11) (istruire) le nuove generazioni dovrà valorizzare la cura _____ (12) la sopraffazione. Pur _____ (13) (essere) fragili, non siamo impotenti. Un'etica rinnovata deve _____ (14) (riconoscere) i vincoli come condizione, non _____ (15) un ostacolo. _____ (16) più misura abitiamo il pianeta, tanto più ne preserviamo la fecondità. La tecnica, _____ (17) (applicare) senza saggezza, rischia di tradirci. _____ (18) la retorica, occorre coerenza tra sapere e agire. _____ (19) il disastro senza mutare stili di vita è la forma più seducente di ipocrisia. Accettando _____ (20) nostra fragilità potremo abitare con misura il pianeta che ci ospita. Tale consapevolezza _____ (21) (dovere) tradursi in policy concrete. _____ (22) essa dipende la credibilità delle istituzioni. _____ (23) realizzare ciò servono passi audaci e lungimiranti.""",
            "answers": ["ci","quale","che","di","mentre","stessa","più","che","Se","riconosca","istruisce","anziché","essendo","riconoscere","come","Con","applicata","Oltre","Denunciare","la","deve","Da","Per"]},
         "rewrite": [
            {"prompt": "1. Trasforma in forma passiva con agente: «L'Antropocene ha posto fine all'illusione del dominio.»", "ref": "L'illusione del dominio è stata posta fine dall'Antropocene."},
            {"prompt": "2. Riscrivi con «al punto che»: «L'uomo domina la natura. La natura ne soffre.»", "ref": "L'uomo domina la natura al punto che questa ne soffre."},
            {"prompt": "3. Unisci con un participio presente: «L'autore denuncia l'antropocentrismo. Egli confonde dominio e libertà.»", "ref": "Denunciando l'antropocentrismo, l'autore confonde dominio e libertà."},
            {"prompt": "4. Esprimi con il periodo ipotetico (II tipo): «Cambiamo stili di vita, dunque il pianeta respira.»", "ref": "Se cambiassimo stili di vita, il pianeta respirerebbe."},
            {"prompt": "5. Riscrivi con «a meno che»: «Cambiamo subito. Perdiamo tutto.»", "ref": "A meno che non cambiamo subito, perderemo tutto."},
            {"prompt": "6. Trasforma in forma passiva: «Non dobbiamo negare la dipendenza.»", "ref": "La dipendenza non deve essere negata."},
            {"prompt": "7. Riscrivi con «in quanto»: «L'etica è necessaria. L'etica fonda la sopravvivenza.»", "ref": "L'etica è necessaria, in quanto fonda la sopravvivenza."},
         ],
         "wordform": [
            {"text": "1. Sostantivo da «dipendere»: la _____ (dipendenza).", "answers": ["dipendenza"]},
            {"text": "2. Aggettivo da «etica»: un approccio _____ (etico).", "answers": ["etico"]},
            {"text": "3. Avverbio da «rapido»: agire _____ (rapidamente).", "answers": ["rapidamente"]},
            {"text": "4. Opposto concettuale di «antropocentrismo»: _____ (ecocentrismo).", "answers": ["ecocentrismo"]},
            {"text": "5. È necessario che l'umanità _____ (riconoscere) i propri limiti planetari.", "answers": ["riconosca"]},
            {"text": "6. Se avessimo agito prima, oggi _____ (esserci) meno disastri.", "answers": ["ci sarebbero"]},
            {"text": "7. La tecnica, _____ (applicare) senza saggezza, rischia di tradirci.", "answers": ["applicata"]},
            {"text": "8. Non _____ (ostante / ostante che) i progressi, il declino continua.", "answers": ["ostante"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力，权重 15%）",
         "items": [
            {"type": "mc", "prompt": "1. (tema) Il relatore definisce l'Antropocene…", "options": ["una scoperta", "una resa di conti", "un successo", "un errore giovane"], "answer": 1},
            {"type": "mc", "prompt": "2. (atteggiamento) Verso il \"dominio della natura\" è…", "options": ["favorevole", "critico", "indifferente", "entusiasta"], "answer": 1},
            {"type": "mc", "prompt": "3. (inferenza) «fattura arriva» significa…", "options": ["paghiamo le conseguenze", "guadagniamo", "nulla", "vendiamo"], "answer": 0},
            {"type": "open", "prompt": "4. (open) Secondo il relatore, chi siamo rispetto al pianeta?", "ref": "Non siamo padroni, siamo ospiti provvisori.", "rows": 2},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语，权重 25%）",
         "tasks": [
            {"desc":
"""抽象话题（哲学 / 艺术 / 社会伦理）演讲 + 批判性质疑回应。
Task：① 准备 3 分钟演讲：\"L'Antropocene ha concluso l'era dell'antropocentrismo?\"；② 考官提出质疑（es. \"Ma senza tecnica non sopravviviamo: è davvero finita l'idea di dominio?\"），你需批判性地回应并捍卫立场。""",
             "points": 50,
             "rubric":
"""① 演讲结构严谨、抽象概念清晰；② 语域学术、词汇精准（tellurico, provvisorio, misura）；③ 批判性回应质疑、逻辑自洽；④ 语法复杂且准确（虚拟 / 条件 / 被动 / 关系）；⑤ 流利度与思辨深度。""",
             "dims": [
                ("Pronuncia 发音", "发音精准，学术语域自如"),
                ("Fluenza 流利度", "演讲连贯，抽象概念流转自然"),
                ("Grammatica 语法", "复杂句法准确（虚拟 / 条件 / 被动 / 关系）"),
                ("Contenuto 内容", "抽象概念清晰，词汇精准（tellurico, provvisorio, misura）"),
                ("Pensiero critico 思辨", "批判性回应质疑，逻辑自洽有深度"),
             ],
             "ref":
"""L'Antropocene non ha concluso l'era dell'antropocentrismo: ne ha soltanto rivelato, con violenza, la crisi. Siamo diventati una forza tellurica, capaci di riplasmare atmosfere e fondali, eppure continuiamo a confondere il dominio con la libertà. L'idea che la natura sia un magazzino infinito a nostra disposizione non è morta; si è solo tradotta in una gestione più tecnica, più efficiente, ma non più umile.

A chi obietta che senza tecnica non sopravviviamo, rispondo: la tecnica senza saggezza ci tradisce. Non serve tornare indietro né rinnegare la conoscenza; serve abitare con misura. L'etica non è un accessorio della coscienza, è la grammatica stessa della sopravvivenza. Negare la nostra dipendenza dal vivente è la forma più raffinata di antropocentrismo.

Dunque l'Antropocene ci consegna un paradosso: proprio mentre celebrano il trionfo della tecnica, le nostre società scoprono di essere ostaggi del proprio successo. La risposta non è il dominio, ma la custodia provvisoria. Non siamo padroni del pianeta; siamo ospiti, e ospiti consapevoli. Fino a che non accetteremo la nostra fragilità — ontologica prima che materiale — l'idea di dominio resterà, pericolosamente, intatta. Solo misurando le nostre pretese potremo preservare la fecondità di ciò che ci ospita."""},
         ]},
    ],
})

# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def _shuffle_options(opts, seed):
    """Deterministic option shuffle so the correct answer lands at varying
    positions (A/B/C/D) instead of always the same letter. The correct option
    CONTENT is preserved; only its display position changes."""
    order = list(range(len(opts)))
    hsh = int.from_bytes(hashlib.md5(seed.encode("utf-8")).digest(), "big")
    random.Random(hsh).shuffle(order)
    return [opts[i] for i in order], order

def render_q(item, qid):
    t = item["type"]
    if t in ("mc", "tf"):
        ans = item["answer"]; opts = item["options"]; ctext = opts[ans]
        sopts, order = _shuffle_options(opts, item.get("prompt", "") + "||" + "||".join(map(str, opts)))
        new_ans = order.index(ans)
        h = '<div class="q-item" data-type="%s" data-correct="%s" data-ctext="%s">' % (t, new_ans, esc(ctext))
        h += '<p class="q-stem">%s</p><div class="opts">' % esc(item["prompt"])
        for i, o in enumerate(sopts):
            h += '<label class="opt"><input type="radio" name="%s" value="%d"> %s</label>' % (qid, i, esc(o))
        h += '</div></div>'
        return h
    if t == "match":
        ans = item["answer"]; opts = item["options"]; ctext = opts[ans]
        sopts, _ = _shuffle_options(opts, item.get("prompt", "") + "||" + "||".join(map(str, opts)))
        h = '<div class="q-item" data-type="match" data-correct="%s" data-ctext="%s">' % (esc(ctext), esc(ctext))
        h += '<p class="q-stem">%s</p><select class="match-sel"><option value="">— scegli —</option>' % esc(item["prompt"])
        for o in sopts:
            h += '<option value="%s">%s</option>' % (esc(o), esc(o))
        h += '</select></div>'
        return h
    if t == "cloze":
        h = '<div class="q-item" data-type="cloze">'
        if item.get("prompt"):
            h += '<p class="q-stem">%s</p>' % esc(item["prompt"])
        frags = item["text"].split("_____")
        ans = item["answers"]
        for i, frag in enumerate(frags):
            h += '<span>%s</span>' % esc(frag)
            if i < len(ans):
                h += '<input class="blank" type="text" size="11" data-correct="%s">' % esc(ans[i])
        h += '</div>'
        return h
    if t == "open":
        h = '<div class="q-item q-subj" data-type="open">'
        h += '<p class="q-stem">%s</p>' % esc(item["prompt"])
        h += '<textarea class="ans" rows="%d" placeholder="La tua risposta..."></textarea>' % item.get("rows", 3)
        h += '<div class="ref" hidden><b>Risposta di riferimento：</b><br>%s</div>' % esc(item["ref"])
        h += '</div>'
        return h
    if t in ("write", "rewrite", "oral_ref"):
        return ""
    # fallback
    return ""

def render_big_cloze(cloze):
    txt = cloze["cloze_text"]; answers = cloze["answers"]
    parts = re.split(r"\((\d+)\)", txt)
    h = '<div class="q-item" data-type="cloze"><div class="cloze-text">'
    for i, seg in enumerate(parts):
        if i % 2 == 0:
            h += '<span>%s</span>' % esc(re.sub(r"_+", "", seg).strip())
        else:
            a = answers[int(seg) - 1]
            h += '<input class="blank" type="text" size="9" data-correct="%s">' % esc(a)
    h += '</div></div>'
    return h

def render_section(sec, lv):
    kind = sec["kind"]
    h = '<section class="module"><h2>%s</h2>' % esc(sec["title"])
    if kind == "reading":
        for tx in sec.get("texts", []):
            h += '<div class="text"><h4>%s</h4><pre>%s</pre></div>' % (esc(tx["title"]), esc(tx["body"]))
        h += '<div class="items">'
        for i, it in enumerate(sec["items"]):
            h += render_q(it, "r%d" % i)
        h += '</div>'
    elif kind == "writing":
        h += '<div class="items">'
        for i, tk in enumerate(sec["tasks"]):
            h += '<div class="q-item q-subj" data-type="write"><p class="q-stem"><b>%s</b><br>%s<br><i>字数：%s</i></p>' % (esc(tk["title"]), esc(tk["prompt"]), esc(tk["limit"]))
            h += '<textarea class="ans" rows="9" placeholder="La tua risposta..."></textarea>'
            h += '<div class="ref" hidden><b>写作范例：</b><br>%s</div></div>' % esc(tk["reference"])
        h += '</div>'
    elif kind == "listening":
        for i, sc in enumerate(lv.get("audio", [])):
            key = "%s_%d" % (lv["code"], i)
            mp3 = "audio/%s.mp3" % key
            h += '<div class="audio-block"><h4>🎧 %s</h4>' % esc(sc["title"])
            if os.path.exists(audio_path(key)):
                h += '<audio controls preload="none" src="%s" type="audio/mpeg"></audio>' % mp3
            else:
                h += '<p class="noaudio">🔇 音频未能生成（需联网调用 edge-tts）。请对照下方原文自测。</p>'
            h += '<details class="transcript"><summary><span class="t-closed">📝 显示听力原文</span><span class="t-open">📝 隐藏听力原文</span></summary><pre>%s</pre></details></div>' % esc(sc["body"])
        h += '<div class="items">'
        for i, it in enumerate(sec["items"]):
            h += render_q(it, "l%d" % i)
        h += '</div>'
    elif kind == "oral":
        h += '<div class="items">'
        for i, tk in enumerate(sec["tasks"]):
            h += '<div class="q-item q-oral" data-type="oral"><p class="q-stem">%s</p>' % esc(tk["desc"])
            # 评分维度 + 评分说明（默认可见，便于对照学习）
            h += '<div class="oral-scoring">'
            h += '<div class="score-head">📋 评分维度 · Criteri di valutazione（满分 %d 分）</div>' % tk["points"]
            h += '<ul class="dims">'
            for lbl, d in tk.get("dims", []):
                h += '<li><b>%s</b> — %s</li>' % (esc(lbl), esc(d))
            h += '</ul>'
            if tk.get("rubric"):
                h += '<div class="rubric-note"><b>评分说明：</b>%s</div>' % esc(tk["rubric"])
            h += '</div>'
            # 参考答案 + 音频
            if tk.get("ref"):
                key = "%s_oral_%d" % (lv["code"], i)
                mp3 = "audio/%s.mp3" % key
                h += '<div class="oral-ref">'
                h += '<div class="ref-head">🗣️ 参考答案 <span class="ref-it">Risposta di riferimento</span></div>'
                if os.path.exists(audio_path(key)):
                    h += '<audio controls preload="none" src="%s" type="audio/mpeg"></audio>' % mp3
                else:
                    h += '<p class="noaudio">🔇 参考答案音频未能生成（需联网调用 edge-tts）。</p>'
                h += '<details class="otranscript"><summary><span class="o-closed">📝 显示参考答案原文</span><span class="o-open">📝 隐藏参考答案原文</span></summary><pre>%s</pre></details></div>' % esc(tk["ref"])
            h += '</div>'
        h += '</div>'
    elif kind == "linguistic":
        cl = sec.get("cloze")
        if cl:
            h += '<h3>C.1 — Cloze senza opzioni（无选项完形，共 %d 空）</h3>' % len(cl["answers"])
            h += render_big_cloze(cl)
        rw = sec.get("rewrite")
        if rw:
            h += '<h3>C.2 — Ristrutturazione / riscrittura di frasi（句子重组/改写）</h3><div class="items">'
            for i, it in enumerate(rw):
                h += '<div class="q-item q-subj" data-type="rewrite"><p class="q-stem">%s</p>' % esc(it["prompt"])
                h += '<textarea class="ans" rows="3" placeholder="La tua risposta..."></textarea>'
                h += '<div class="ref" hidden><b>参考答案：</b><br>%s</div></div>' % esc(it["ref"])
            h += '</div>'
        wf = sec.get("wordform")
        if wf:
            h += '<h3>C.3 — Forma della parola / modo verbale（词形/语式填空）</h3><div class="items">'
            for it in wf:
                h += render_q({"type": "cloze", "text": it["text"], "answers": it["answers"]}, "wf")
            h += '</div>'
    h += '</section>'
    return h

CSS = """
:root{--wine:#7b1e2b;--wine2:#a83246;--ink:#23211f;--paper:#fbf8f4;--line:#e4ddd2;--ok:#1b7a3d;--no:#c0392b;}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,"Segoe UI",Roboto,"Helvetica Neue","PingFang SC","Microsoft YaHei",sans-serif;color:var(--ink);background:var(--paper);line-height:1.65}
header.top{background:linear-gradient(135deg,var(--wine),var(--wine2));color:#fff;padding:26px 20px;box-shadow:0 2px 10px rgba(0,0,0,.15)}
header.top .topnav{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:4px}header.top .back{color:#ffd9df;text-decoration:none;font-size:14px}header.top .back:hover{text-decoration:underline;opacity:.85}
header.top .ttl{font-size:26px;font-weight:800;margin-top:6px}
header.top .ttl .lvl{display:inline-block;background:#fff;color:var(--wine);border-radius:8px;padding:2px 10px;margin-right:10px;font-size:20px}
header.top .sub{opacity:.9;margin-top:4px;font-size:15px}
main{max-width:880px;margin:0 auto;padding:24px 18px 120px}
section.module{margin:30px 0;background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px 22px;box-shadow:0 1px 4px rgba(0,0,0,.04)}
section.module h2{margin:0 0 14px;color:var(--wine);font-size:20px;border-bottom:2px solid var(--line);padding-bottom:8px}
section.module h3{color:#444;font-size:16px;margin:22px 0 10px}
.text{background:#f6f1e9;border-left:4px solid var(--wine);border-radius:8px;padding:12px 14px;margin:12px 0}
.text h4{margin:0 0 6px;font-size:14px;color:var(--wine)}
pre{white-space:pre-wrap;margin:0;font-family:"Courier New",monospace;font-size:14px}
.items{margin-top:14px}
.q-item{margin:14px 0;padding:12px 14px;border:1px solid var(--line);border-radius:10px;background:#fffdf9}
.q-item.correct{border-color:var(--ok);background:#f1faf3}
.q-item.wrong{border-color:var(--no);background:#fdf1f0}
.q-stem{margin:0 0 8px;font-weight:600}
.opts{display:flex;flex-direction:column;gap:6px}
.opt{display:flex;align-items:center;gap:8px;cursor:pointer;padding:4px 6px;border-radius:6px}
.opt:hover{background:#f3ede3}
.match-sel{font-size:15px;padding:5px 8px;border-radius:6px;border:1px solid #bbb;margin-top:4px}
.blank{font-size:15px;padding:3px 6px;border:1px solid #bbb;border-radius:6px;margin:0 4px}
.blank.correct{border-color:var(--ok);background:#eafaf0}
.blank.wrong{border-color:var(--no);background:#fdeceb}
.anshint{color:var(--no);font-size:13px;margin-left:6px}
textarea.ans{width:100%;font-size:15px;padding:10px;border:1px solid #ccc;border-radius:8px;font-family:inherit;resize:vertical}
.q-subj .ref{margin-top:10px;padding:10px 12px;background:#eef6fb;border-left:4px solid #2a7fb8;border-radius:8px;font-size:14px}
.q-note{margin-top:8px;font-weight:700;font-size:14px}
.q-note.ok{color:var(--ok)} .q-note.no{color:var(--no)}
.audio-block{background:#f0f4f7;border:1px solid #cfe0ea;border-radius:10px;padding:12px 14px;margin:12px 0}
.audio-block h4{margin:0 0 8px;color:#1f5f80}
audio{width:100%;margin-bottom:8px;display:block}
.noaudio{color:#b06a00;font-weight:600}
/* ---- 口语题评分系统 ---- */
.q-oral{background:#fbf7ef;border:1px solid #ecd9b0;border-radius:12px;padding:16px 18px;margin:14px 0}
.q-oral .q-stem{margin:0 0 12px;font-size:15px;line-height:1.7;white-space:pre-wrap}
.oral-scoring{background:#fff;border:1px solid #e7dcc4;border-radius:10px;padding:12px 14px;margin-bottom:12px}
.score-head{font-weight:700;color:#9a6b00;margin-bottom:8px;font-size:14px}
.dims{margin:0;padding-left:20px;font-size:14px;line-height:1.9}
.dims li{margin-bottom:2px}
.rubric-note{margin-top:8px;padding-top:8px;border-top:1px dashed #e0d3b6;font-size:13px;color:#5a4a2a;line-height:1.7}
.oral-ref{background:#eef6fb;border:1px solid #cfe0ea;border-radius:10px;padding:12px 14px}
.ref-head{font-weight:700;color:#1f5f80;margin-bottom:8px;font-size:14px}
.ref-it{font-weight:400;color:#5b87a0;font-style:italic;font-size:12px}
.oral-ref pre{margin:8px 0 0;white-space:pre-wrap;word-break:break-word;font-size:14px;line-height:1.75;background:#fff;border:1px solid #dce8f0;border-radius:8px;padding:10px 12px}
/* 口语参考答案原文折叠 */
.otranscript{margin-top:8px}
.otranscript summary{cursor:pointer;color:#1f5f80;font-weight:600;font-size:13px;user-select:none;list-style:none}
.otranscript summary::-webkit-details-marker{display:none}
.otranscript .o-open{display:none}
.otranscript[open] .o-closed{display:none}
.otranscript[open] .o-open{display:inline}
.transcript{margin-top:10px}
.transcript summary{cursor:pointer;color:#1f5f80;font-weight:600;font-size:14px;user-select:none;list-style:none}
.transcript summary::-webkit-details-marker{display:none}
.transcript summary:hover{text-decoration:underline}
.transcript .t-open{display:none}
.transcript[open] .t-closed{display:none}
.transcript[open] .t-open{display:inline}
.transcript[open] summary{margin-bottom:8px}
.transcript pre{margin-top:0}
#btn-check{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);background:var(--wine);color:#fff;border:none;font-size:17px;font-weight:700;padding:13px 30px;border-radius:30px;cursor:pointer;box-shadow:0 4px 14px rgba(123,30,43,.4);z-index:10}
#btn-check:hover{background:var(--wine2)}
#btn-reset{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);margin-left:170px;background:#555;color:#fff;border:none;font-size:15px;padding:13px 22px;border-radius:30px;cursor:pointer;z-index:10}
#result{margin-top:20px;padding:18px 20px;border-radius:12px;background:#fff;border:2px solid var(--wine);text-align:center}
.res-score{font-size:18px;margin-bottom:10px}
.res-grade{display:inline-block;color:#fff;font-weight:800;font-size:22px;padding:6px 22px;border-radius:10px;margin-bottom:8px}
.res-note{font-size:14px;color:#555;margin-top:8px}
.index-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px;margin-top:20px}
.card{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:0 1px 4px rgba(0,0,0,.05);transition:.15s}
.card:hover{transform:translateY(-3px);border-color:var(--wine)}
.card .lvl{display:inline-block;background:var(--wine);color:#fff;border-radius:8px;padding:3px 12px;font-weight:800;font-size:18px}
.card .nm{font-weight:700;margin:8px 0 4px;font-size:16px}
.card .sb{font-size:13px;color:#666}
.intro{max-width:880px;margin:24px auto;padding:0 18px;color:#555}
"""

JS = """
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]/g,'');}
function gradeOf(p){if(p>=85)return['Eccellente','#1b7a3d'];if(p>=70)return['Buono','#2e7d32'];if(p>=55)return['Discreto','#b8860b'];if(p>=40)return['Insufficiente','#c0392b'];return['Grave','#7b1e2b'];}
function verifica(){
  var items=document.querySelectorAll('.q-item');
  var score=0,total=0;
  items.forEach(function(el){
    var t=el.dataset.type;
    if(t==='mc'||t==='tf'||t==='match'){
      total++;
      var ok=false,corr=el.dataset.correct;
      if(t==='match'){var sel=el.querySelector('select');if(sel&&sel.value===corr)ok=true;}
      else{var inp=el.querySelector('input:checked');if(inp&&inp.value===corr)ok=true;}
      el.classList.add(ok?'correct':'wrong');
      var n=document.createElement('div');n.className='q-note '+(ok?'ok':'no');
      n.textContent=ok?'✅ Corretto':'❌ Risposta corretta: '+el.dataset.ctext;
      el.appendChild(n);
      el.querySelectorAll('input,select').forEach(function(i){i.disabled=true;});
    } else if(t==='cloze'){
      el.querySelectorAll('input.blank').forEach(function(inp){
        total++;
        var v=norm(inp.value);
        var ok2=v.length>0 && v.indexOf(norm(inp.dataset.correct))>=0;
        if(ok2)score++;
        inp.classList.add(ok2?'correct':'wrong');
        if(!ok2){var s=document.createElement('span');s.className='anshint';s.textContent=' ✓ '+inp.dataset.correct;inp.insertAdjacentElement('afterend',s);}
        inp.disabled=true;
      });
    }
  });
  document.querySelectorAll('.q-subj').forEach(function(el){var r=el.querySelector('.ref');if(r)r.hidden=false;});
  var pct= total? Math.round(score/total*100):0;
  var g=gradeOf(pct);
  var box=document.getElementById('result');
  box.hidden=false;
  box.innerHTML='<div class="res-score">客观题正确率：<b>'+score+' / '+total+'</b> （'+pct+'%）</div>'+
    '<div class="res-grade" style="background:'+g[1]+'">'+g[0]+'</div>'+
    '<div class="res-note">写作 / 口语 / 改写 / 开放题请对照上方参考答案与评分要点自评（本卷主观题满分 '+SUBJMAX+' 分）。</div>';
  box.scrollIntoView({behavior:'smooth'});
  document.getElementById('btn-check').hidden=true;
  document.getElementById('btn-reset').hidden=false;
}
function resetta(){location.reload();}
// 单一播放：播放任意音频时自动打断其他正在播放的音频，避免重叠
document.addEventListener('play', function(e){
  if(e.target && e.target.tagName === 'AUDIO'){
    document.querySelectorAll('audio').forEach(function(a){ if(a!==e.target) a.pause(); });
  }
}, true);
"""

def build_page(lv):
    body = ""
    for sec in lv["sections"]:
        body += render_section(sec, lv)
    return """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CELI {code} — {name}</title>
<style>{css}</style>
</head>
<body>
<header class="top">
  <nav class="topnav"><a href="index.html" class="back">← Indice CELI Vol.1</a><a href="../CELI.html" class="back">🏠 CELI 导航页</a></nav>
  <div class="ttl"><span class="lvl">{code}</span> {name}</div>
  <div class="sub">{subtitle} · {theme}</div>
</header>
<main>
<p class="intro">本卷主题：环境、气候与可持续发展。听力为模拟音频文本（由考官/录音播放），本页已用真人意大利语发音（edge-tts）生成音频，点击 ▶ 即可播放自测。提交后客观题自动判分，写作/口语/改写/开放题展开参考答案与评分要点供自评。</p>
{body}
<button id="btn-check" onclick="verifica()">Verifica le risposte（提交判分）</button>
<button id="btn-reset" hidden onclick="resetta()">Ricomincia（重做）</button>
<div id="result" hidden></div>
</main>
<script>var SUBJMAX={subj_max};
{js}</script>
</body>
</html>""".format(css=CSS, code=lv["code"], name=lv["name"], subtitle=lv["subtitle"],
                 theme=lv["theme"], subj_max=lv["subj_max"], body=body, js=JS)

def build_index(levels):
    cards = ""
    for lv in levels:
        cards += '<a class="card" href="%s.html"><span class="lvl">%s</span><div class="nm">%s</div><div class="sb">%s</div></a>' % (
            lv["code"], lv["code"], esc(lv["name"]), esc(lv["subtitle"]))
    return """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CELI 模拟题库 · 第1卷（A1–C2）</title>
<style>{css}</style>
</head>
<body>
<header class="top">
  <div class="ttl">CELI 模拟题库 · 第1卷</div>
  <div class="sub">🌱 Ambiente, clima e sostenibilità — 六个等级（A1–C2）考试页面</div>
</header>
<main>
<p class="intro">本卷严格按 CELI（佩鲁贾 CVCL）近年真题模块结构命题，宏观主题为「环境、气候与可持续发展」，六级子主题螺旋上升。点击任意等级进入对应考试页面：含阅读、写作、听力（真人发音音频）、口语，B2/C1/C2 另含「语言能力」模块。提交后客观题自动判分。</p>
<div class="index-grid">{cards}</div>
</main>
</body>
</html>""".format(css=CSS, cards=cards)

def main():
    os.makedirs(OUT, exist_ok=True)
    print("Generating audio...")
    gen_all(LEVELS)
    for lv in LEVELS:
        html = build_page(lv)
        with open(os.path.join(OUT, "%s.html" % lv["code"]), "w", encoding="utf-8") as f:
            f.write(html)
        print("WROTE", lv["code"], len(html))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index(LEVELS))
    print("WROTE index")
    print("AUDIO DIR:", AUDIO_DIR)

if __name__ == "__main__":
    main()

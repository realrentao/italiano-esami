# -*- coding: utf-8 -*-
"""Dati strutturati del Vol.3 degli esami CELI (A1-C2).
Tema: Lavoro, occupazione e carriera (工作、就业与远程办公).
Questo modulo è consumato dal generatore (generator_template.py): la
struttura di LEVELS, sections, items e campi è identica a quella attesa
dal motore di rendering.
"""

VOL_NO = 3
THEME_EMOJI = "💼"
THEME_TEXT = "Lavoro, occupazione e carriera"

LEVELS = []

# ============================== A1 =========================================
LEVELS.append({
    "code": "A1", "name": "CELI Impatto",
    "subtitle": "il mio lavoro / un colloquio semplice",
    "theme": "💼 Lavoro, occupazione e carriera", "subj_max": 20,
    "audio": [],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo 1 — Messaggio di Luca", "body":
"""Ciao! Mi chiamo Luca e lavoro in una panetteria. Apro il negozio alle 7.00 e chiudo alle 13.00. Il mercoledì riposo. Abito a Firenze con i miei genitori. Luca"""},
            {"title": "Testo 2 — Annuncio", "body":
"""CERCHIAMO cuoca/e per il nostro ristorante. Lavoro di giorno, 5 giorni a settimana. Paga: 12 euro l'ora. Telefono: 347 987 6543."""},
            {"title": "Testo 3 — Biglietto di Sara", "body":
"""Cara nonna, oggi ho un colloquio di lavoro alle 9.30. Sono un po' nervosa ma felice! Baci, Sara."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Luca lavora in：", "options": ["A) un ristorante", "B) una panetteria", "C) un ufficio"], "answer": 1},
            {"type": "mc", "prompt": "2. Luca riposa di：", "options": ["A) lunedì", "B) mercoledì", "C) domenica"], "answer": 1},
            {"type": "mc", "prompt": "3. Sara ha il colloquio：", "options": ["A) alle 9.30", "B) alle 7.00", "C) alle 13.00"], "answer": 0},
            {"type": "mc", "prompt": "4. Nella panetteria, Luca chiude alle：", "options": ["A) 7.00", "B) 13.00", "C) 9.30"], "answer": 1},
            {"type": "mc", "prompt": "5. La cuoca guadagna：", "options": ["A) 10 euro", "B) 12 euro", "C) 5 euro"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Scrivi una cartolina a un amico/a（明信片 / 留言）",
             "prompt": "Scrivi una cartolina a un tuo amico/a. Parla del tuo lavoro OPPURE di un colloquio di lavoro. Scrivi 2–3 frasi (30–50 parole). Usa il presente. Ricorda: inizia con \"Ciao [nome]!\" e firma in fondo.",
             "limit": "30–50 词",
             "reference":
"""Ciao Marco! Lavoro in un bar a Roma. Apro il bar alle 8.00 e preparo i caffè. Il sabato ho un colloquio per un nuovo lavoro. Sono contento! Un abbraccio, Luca."""},
         ]},
        {"kind": "oral", "title": "3. Prova orale（口语，含听力评定）",
         "tasks": [
            {"desc":
"""CELI A1 无独立听力卷，听力并入口语评定。考官先朗读 1–2 句简单指示（模拟音频文本），考生听懂并回应，再进入引导问答。
① 考官引导问答（姓名 / 年龄 / 住址 / 家庭 / 工作）；② 用 2–3 句介绍自己典型的一天。
示例问句：
1. Come ti chiami? / Quanti anni hai?
2. Dove abiti?
3. Lavori o studi?
4. Che lavoro fai?
5. Ti piace il tuo lavoro? Perché?""",
             "points": 20,
             "rubric":
"""① 听懂简单指令并反应；② 用基本词汇与单句作答；③ 发音可懂、语调自然；④ 互动积极、能维持简短交流。达到 11 分即通过。""",
             "dims": [
                ("Pronuncia 发音", "单音基本准确，语调自然，能听懂简单指令"),
                ("Fluenza 流利度", "能用基本词汇与单句作答，自我介绍连贯"),
                ("Grammatica 语法", "使用基础句型(essere/avere/presente)，错误不影响理解"),
                ("Contenuto 内容", "覆盖姓名 / 年龄 / 住址 / 工作习惯等任务要求"),
                ("Interazione 互动", "能回应考官提问，维持简短交流"),
             ],
             "ref":
"""Buongiorno, mi chiamo Luca e ho vent'anni. Lavoro in un bar a Roma: apro il bar alle otto e preparo i caffè. Il sabato mattina ho un colloquio per un nuovo lavoro, sono un po' nervoso ma felice. Abito con i miei genitori e mi piace leggere. La sera guardo la TV e poi vado a dormire. Secondo me è importante avere un lavoro che ti piace. E tu, che lavoro fai?"""},
         ]},
    ],
})

# ============================== A2 =========================================
LEVELS.append({
    "code": "A2", "name": "CELI 1",
    "subtitle": "cercare lavoro / un annuncio di lavoro",
    "theme": "💼 Lavoro, occupazione e carriera", "subj_max": 20,
    "audio": [
        {"title": "Dialogo 1 — Telefonata", "body":
"""A: Pronto, è l'ufficio lavoro?
B: Sì. Cerchiamo una commessa per un negozio di abbigliamento.
A: Io ho esperienza! Lavoro da due anni in un negozio.
B: Bene, venga lunedì alle 10 per il colloquio."""},
        {"title": "Dialogo 2 — Annuncio radio", "body":
"""Oggi parliamo di lavoro. Molti giovani cercano un impiego su internet. Un consiglio: siate preparati e non abbiate paura dei colloqui."""},
        {"title": "Dialogo 3 — Storia di Marco", "body":
"""Marco voleva fare il cameriere. Ha inviato 10 CV. Alla fine ha lavorato in un bar vicino a casa. È contento."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo A — Annuncio di lavoro", "body":
"""Cameriere/a cercasi — Ristorante La Torre, Milano
Orario: part-time, solo la sera (18.00–23.00).
Requisiti: conoscenza base dell'inglese, disponibilità nei weekend.
Invia il CV a: lavoro@latorre.it entro il 30 aprile."""},
            {"title": "Testo B — Blog di Giulia", "body":
"""Ho trovato lavoro dopo tre mesi di ricerca! Ogni mattina guardavo gli annunci online e inviavo il CV. Una volta ho fatto un colloquio molto difficile, ma alla fine è andata bene. Il segreto? Essere puntuali e sorridere."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Il ristorante cerca：", "options": ["A) un cuoco", "B) un cameriere", "C) una segretaria"], "answer": 1},
            {"type": "mc", "prompt": "2. Il lavoro è：", "options": ["A) a tempo pieno", "B) solo la sera", "C) solo di giorno"], "answer": 1},
            {"type": "mc", "prompt": "3. Giulia ha trovato lavoro dopo：", "options": ["A) una settimana", "B) tre mesi", "C) un anno"], "answer": 1},
            {"type": "mc", "prompt": "4. Per lavorare alla Torre serve：", "options": ["A) l'inglese", "B) la patente", "C) la laurea"], "answer": 0},
            {"type": "mc", "prompt": "5. Il CV va inviato a：", "options": ["A) un indirizzo email", "B) un fax", "C) un ufficio"], "answer": 0},
            {"type": "mc", "prompt": "6. Secondo Giulia, il segreto è：", "options": ["A) essere ricchi", "B) essere puntuali e sorridere", "C) mentire"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito 1 — Completamenti（补全短文）",
             "prompt": "Completa il testo con le parole: CV / colloquio / annuncio / inviare. \"Ho letto un _____ su internet. Domani ho un _____. Devo _____ il mio _____ per email.\"",
             "limit": "填空",
             "reference": "Ho letto un annuncio su internet. Domani ho un colloquio. Devo inviare il mio CV per email."},
            {"title": "Compito 2 — Espansione（扩写留言，40–60 词）",
             "prompt": "Da questo messaggio breve scrivi un biglietto più lungo (40–60 parole): \"Cara mamma, ho trovato un lavoro! Ti racconto…\"",
             "limit": "40–60 词",
             "reference":
"""Cara mamma, ho trovato un lavoro! Lavoro in una libreria vicino a casa. Il lunedì e il mercoledì aiuto i clienti a scegliere i libri. Il sabato mattina organizzo i nuovi arrivi. Sono molto felice perché mi piace leggere. Ti voglio bene, Giulia."""},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "1. L'ufficio cerca：", "options": ["A) un cuoco", "B) una commessa", "C) un autista"], "answer": 1},
            {"type": "mc", "prompt": "2. Il colloquio è di：", "options": ["A) lunedì", "B) martedì", "C) domenica"], "answer": 0},
            {"type": "mc", "prompt": "3. La ragazza ha esperienza di：", "options": ["A) 1 anno", "B) 2 anni", "C) 5 anni"], "answer": 1},
            {"type": "mc", "prompt": "4. Dove cercano lavoro molti giovani?", "options": ["A) al giornale", "B) su internet", "C) in tv"], "answer": 1},
            {"type": "mc", "prompt": "5. Marco ha inviato：", "options": ["A) 5 CV", "B) 10 CV", "C) 20 CV"], "answer": 1},
            {"type": "mc", "prompt": "6. Marco alla fine lavora：", "options": ["A) in un ristorante lontano", "B) in un bar vicino a casa", "C) in ufficio"], "answer": 1},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 自我介绍 + 习惯爱好；② 描述图片（求职者在办公室面试：dov'è? che fa? com'è?）；③ 角色扮演：你是求职者，考官是老板，问 "Perché vuole questo lavoro?" / "Ha esperienza?"。
示例：Presentati (nome, età, da dove vieni, che fai, hobby). Descrivi la foto: una persona in ufficio, seduta, seria. Rispondi al datore di lavoro con frasi semplici.""",
             "points": 20,
             "rubric":
"""① 自我介绍流利，presente / passato prossimo 基本正确；② 图片描述含方位、动作、形容词；③ 角色扮演能回应老板提问，用 perché + presente 给出理由；④ 词汇覆盖 lavoro / colloquio / esperienza。""",
             "dims": [
                ("Pronuncia 发音", "发音清晰，重音基本正确"),
                ("Fluenza 流利度", "自我介绍流畅，含个人习惯与爱好"),
                ("Grammatica 语法", "现在时 / 近过去时使用基本正确"),
                ("Contenuto 内容", "涵盖自我介绍、图片描述、角色扮演三项任务"),
                ("Interazione 互动", "角色扮演用语得体，完成信息询问"),
             ],
             "ref":
"""Buongiorno, mi presento: mi chiamo Giulia, ho ventiquattro anni e vengo da Bologna. Studio e lavoro part-time in una libreria. Nel weekend mi piace leggere e andare in bicicletta. Nella foto vedo un colloquio di lavoro: una persona è seduta in un ufficio, davanti a una scrivania, e parla con il datore di lavoro. Sembra seria ma tranquilla. Perché voglio questo lavoro? Perché mi piace stare con i clienti e imparare cose nuove, e ho già esperienza in un negozio."""},
         ]},
    ],
})

# ============================== B1 =========================================
LEVELS.append({
    "code": "B1", "name": "CELI 2",
    "subtitle": "lo smart working / conciliare vita e lavoro",
    "theme": "💼 Lavoro, occupazione e carriera", "subj_max": 30,
    "audio": [
        {"title": "Servizio radio — Lo smart working", "body":
"""In Italia lo smart working è cresciuto molto durante la pandemia. Oggi il 40% delle aziende lo offre ai dipendenti. Secondo uno studio, chi lavora da casa risparmia due ore al giorno di trasporto. Ma attenzione: senza regole, il confine tra vita e lavoro scompare."""},
        {"title": "Intervista — Sofia", "body":
"""Io sono mamma e lavoro da casa tre giorni a settimana. Prima ero sempre stanca perché passavo tre ore in treno. Ora preparo la colazione ai bambini e poi mi metto al computer. Il problema? La sera continuo a controllare le email."""},
        {"title": "Dialogo — Padre e figlio", "body":
"""— Papà, stasera giochiamo?
— No, devo finire un report. Domani, promesso!"""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo 1 — Email aziendale（smart working）", "body":
"""Da: ufficio personale@azienda.it
A: tutti i dipendenti
Oggetto: Nuova regola sullo smart working
A partire da maggio, ogni dipendente può lavorare da casa due giorni alla settimana. Chi è interessato deve compilare il modulo online entro venerdì. Lo smart working aiuta a conciliare vita e lavoro, specialmente per chi ha figli piccoli."""},
            {"title": "Testo 2 — Volantino sindacale", "body":
"""Lo smart working è un diritto, non un favore. Chiediamo orari flessibili e un welfare che sostenga le famiglie. Sciopero nazionale il 10 maggio."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Da quando si può fare smart working?", "options": ["A) da aprile", "B) da maggio", "C) da giugno"], "answer": 1},
            {"type": "mc", "prompt": "2. Quanti giorni a settimana?", "options": ["A) uno", "B) due", "C) tre"], "answer": 1},
            {"type": "mc", "prompt": "3. Il modulo va inviato entro：", "options": ["A) venerdì", "B) sabato", "C) domenica"], "answer": 0},
            {"type": "match", "prompt": "4. Testo 1 →", "options": ["A) una protesta sindacale", "B) una comunicazione aziendale"], "answer": 1},
            {"type": "match", "prompt": "5. Testo 2 →", "options": ["A) una protesta sindacale", "B) una comunicazione aziendale"], "answer": 0},
            {"type": "cloze", "text": "6. Lo smart working serve a _____ vita e lavoro.", "answers": ["conciliare"]},
            {"type": "cloze", "text": "7. Il sindacato chiede orari _____.", "answers": ["flessibili"]},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito 1 — Questionario（问卷，60–80 词）",
             "prompt": "Compila il questionario sulla tua esperienza di smart working: Nome / Età / Professione; Fai smart working? Sì/No; Quanti giorni a settimana?; Secondo te, quali sono i vantaggi e gli svantaggi? (scrivi 3–4 frasi)",
             "limit": "60–80 词",
             "reference":
"""Nome: Elena, 34 anni, grafica. Faccio smart working sì, 3 giorni a settimana. Vantaggi: risparmio tempo e sto più con mia figlia. Svantaggi: a volte mi distraggo e lavoro fino a tardi. Penso che servano regole chiare, per esempio spegnere il computer alle 18.00."""},
            {"title": "Compito 2 — E-mail（给朋友写邮件，120–150 词）",
             "prompt": "Scrivi a un amico / a un collega. Racconta la prima volta che hai lavorato da casa: cosa è successo, com'era, cosa hai imparato. Usa il passato (passato prossimo / imperfetto).",
             "limit": "120–150 词",
             "reference":
"""Cara Sara, ti racconto la prima volta che ho lavorato da casa. Era il lockdown del 2020: la mia azienda ha chiuso e io ho portato il computer in cucina. All'inizio ero felice perché non prendevo più il treno, ma dopo una settimana mi mancavano i colleghi. Ho imparato a organizzarmi: mi alzavo presto, facevo una lista di cose da fare e facevo pause brevi. La sera, però, faticavo a staccare. Ora capisco che lo smart working è utile, ma serve disciplina per conciliare vita e lavoro. Un abbraccio, Marco."""},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "1. Lo smart working in Italia è cresciuto durante：", "options": ["A) la crisi", "B) la pandemia", "C) le vacanze"], "answer": 1},
            {"type": "mc", "prompt": "2. Oggi quante aziende lo offrono?", "options": ["A) il 20%", "B) il 40%", "C) il 60%"], "answer": 1},
            {"type": "mc", "prompt": "3. Chi lavora da casa risparmia circa：", "options": ["A) 1 ora", "B) 2 ore", "C) 3 ore al giorno"], "answer": 1},
            {"type": "mc", "prompt": "4. Un rischio citato è：", "options": ["A) troppo stipendio", "B) confine vita/lavoro scompare", "C) niente computer"], "answer": 1},
            {"type": "mc", "prompt": "5. Sofia lavora da casa：", "options": ["A) 1 giorno", "B) 2 giorni", "C) 3 giorni"], "answer": 2},
            {"type": "mc", "prompt": "6. Prima Sofia era stanca per：", "options": ["A) il treno", "B) i figli", "C) il capo"], "answer": 0},
            {"type": "mc", "prompt": "7. Il problema di Sofia la sera è：", "options": ["A) la TV", "B) le email", "C) il cane"], "answer": 1},
            {"type": "mc", "prompt": "8. Nel dialogo, il papà non gioca perché：", "options": ["A) piove", "B) finisce un report", "C) dorme"], "answer": 1},
            {"type": "mc", "prompt": "9. Il papà promette di giocare：", "options": ["A) stasera", "B) domani", "C) domenica"], "answer": 1},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 自我介绍 / 兴趣 / 日常；② 描述图片；③ 角色扮演。
任务：① 介绍自己、兴趣与典型一天（usa presente e passato）；② 描述一张照片：una persona davanti al computer a casa, con un bambino vicino（dov'è? cosa fa? com'è la sua giornata?）；③ 角色扮演：Sei un manager，考官问 "Secondo te, lo smart working migliora la vita delle famiglie?" Rispondi con opinioni ed esempi。""",
             "points": 30,
             "rubric":
"""① 自我介绍连贯，presente + passato prossimo/imperfetto 混用正确；② 图片描述有方位、动作与评判；③ 角色扮演能用 secondo me/penso che + 理由与举例；④ 词汇与连接词（perché, ma, invece）运用自然。""",
             "dims": [
                ("Pronuncia 发音", "发音标准，语调节奏自然"),
                ("Fluenza 流利度", "连贯表达观点与习惯，少停顿"),
                ("Grammatica 语法", "现在时 / 近过去时 / imperfetto较准确，尝试复合句"),
                ("Contenuto 内容", "图片描述准确，角色扮演体现观点表达"),
                ("Interazione 互动", "能用secondo me/penso che给出理由与举例"),
             ],
             "ref":
"""Buongiorno, mi chiamo Marco e lavoro come grafico da casa tre giorni a settimana. Nel tempo libero mi piace fotografare e cucinare. Una giornata tipica inizia presto: preparo la colazione, poi mi metto al computer fino a pranzo. Nella foto vedo una mamma davanti al computer a casa, con un bambino vicino che gioca. È comoda perché sta con la famiglia, ma faticosa perché il confine tra lavoro e vita scompare. Secondo me lo smart working migliora la vita delle famiglie: risparmiamo tempo e stiamo più con i figli. Però servono regole chiare, per esempio spegnere il computer alla sera."""},
         ]},
    ],
})

# ============================== B2 =========================================
LEVELS.append({
    "code": "B2", "name": "CELI 3",
    "subtitle": "gig economy / formazione continua",
    "theme": "💼 Lavoro, occupazione e carriera", "subj_max": 50,
    "audio": [
        {"title": "Intervista — Gig economy e formazione", "body":
"""Giornalista: Professore, cos'è la gig economy?
Prof.: È un mercato del lavoro fatto di micro-incarichi. Il vantaggio è la flessibilità; lo svantaggio è la precarietà. I rider, per esempio, non hanno contratto.
G: La formazione può aiutare?
P: Sì, ma serve un sistema pubblico, altrimenti solo i privilegiati studiano."""},
        {"title": "Servizio — Scuola serale per rider", "body":
"""A Milano nasce una scuola serale per rider. Si chiama "Ruota della conoscenza". I corsi sono gratuiti, finanziati dal comune. Obiettivo: insegnare informatica e italiano agli stranieri che fanno consegne. Cento iscritti nel primo mese."""},
        {"title": "Monologo — La vita di una rider", "body":
"""Io faccio la rider da due anni. All'inizio era bello: scelgo io gli orari. Poi ho capito che non ho ferie, non ho malattia. Studio di notte per cambiare vita. Sogno un lavoro vero, con un contratto. La formazione mi sta aiutando: ho fatto un corso di contabilità. Ora invio CV, ma è difficile. Comunque non mollo."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "A.1 — Testo A1a（La gig economy）", "body":
"""Negli ultimi anni la gig economy ha ridisegnato il mercato del lavoro. Rider, driver e freelancer trovano incarichi tramite piattaforme digitali che promettono flessibilità assoluta. Tuttavia, dietro la libertà apparente si nasconde spesso una precarietà strutturale: niente contratto fisso, niente ferie retribuite, né tutela in caso di infortunio. L'algoritmo decide quali consegne assegnare e a quale prezzo, trasformando il lavoratore in un numero ottimizzato. Diversi tribunali europei hanno cominciato a riconoscere ai rider diritti da dipendente, ma la strada è ancora lunga."""},
            {"title": "A.1 — Testo A1b（La formazione continua）", "body":
"""Se il lavoro cambia così velocemente, anche le competenze devono aggiornarsi. È qui che entra in gioco la formazione continua (lifelong learning): corsi brevi, certificazioni digitali e microcredenziali che permettono di restare competitivi. Le aziende più innovative non assumono solo per il titolo di studio, ma per la capacità di apprendere. Tuttavia, il rischio è una nuova diseguaglianza: chi ha tempo e risorse si forma, chi è schiacciato dai turni non può. La formazione continua è una opportunità, ma va resa accessibile a tutti."""},
            {"title": "A.2 — Testo A2a（Il lavoro dei rider）", "body":
"""Il lavoro dei rider nelle città italiane: problemi di sicurezza, incidenti, scioperi per i diritti."""},
            {"title": "A.2 — Testo A2b（I corsi serali dei comuni）", "body":
"""I corsi serali gratuiti offerti dai comuni: informatica, lingue, cucina per adulti che vogliono riqualificarsi."""},
            {"title": "A.3 — Testo（Saggio sul lavoro digitale）", "body":
"""Per sopravvivere alla gig economy, i giovani devono diventare imprenditori di se stessi: gestire il proprio brand, i propri orari e la propria formazione. È una libertà faticosa, ma può essere una scuola di autonomia."""},
         ],
         "items": [
            {"type": "mc", "prompt": "A.1-1. La gig economy offre soprattutto：", "options": ["A) un contratto fisso", "B) flessibilità apparente", "C) ferie retribuite"], "answer": 1},
            {"type": "mc", "prompt": "A.1-2. Chi decide le consegne e i prezzi?", "options": ["A) il sindacato", "B) l'algoritmo", "C) il governo"], "answer": 1},
            {"type": "mc", "prompt": "A.1-3. I rider, secondo i tribunali, iniziano ad avere：", "options": ["A) diritti da dipendente", "B) stipendi bassi", "C) più ferie"], "answer": 0},
            {"type": "mc", "prompt": "A.1-4. La formazione continua serve a：", "options": ["A) prendere una laurea lunga", "B) aggiornare le competenze", "C) smettere di lavorare"], "answer": 1},
            {"type": "mc", "prompt": "A.1-5. Le aziende innovative valorizzano：", "options": ["A) solo il titolo di studio", "B) la capacità di apprendere", "C) l'età anagrafica"], "answer": 1},
            {"type": "mc", "prompt": "A.1-6. Un rischio della formazione continua è：", "options": ["A) troppa equality", "B) una nuova diseguaglianza", "C) pochi corsi"], "answer": 1},
            {"type": "mc", "prompt": "A.1-7. «Schiacciato dai turni» significa：", "options": ["A) libero", "B) oppresso dagli orari", "C) ben pagato"], "answer": 1},
            {"type": "mc", "prompt": "A.1-8. Le microcredenziali sono：", "options": ["A) piccoli prestiti", "B) brevi certificazioni", "C) tasse"], "answer": 1},
            {"type": "mc", "prompt": "A.1-9. Entrambi i testi parlano di：", "options": ["A) vacanze", "B) cambiamento del lavoro", "C) politica"], "answer": 1},
            {"type": "match", "prompt": "A.2-1. Si parla di incidenti stradali.", "options": ["A2a", "A2b"], "answer": 0},
            {"type": "match", "prompt": "A.2-2. Si parla di lezioni di informatica.", "options": ["A2a", "A2b"], "answer": 1},
            {"type": "match", "prompt": "A.2-3. I lavoratori protestano per i diritti.", "options": ["A2a", "A2b"], "answer": 0},
            {"type": "match", "prompt": "A.2-4. I corsi sono gratuiti per gli adulti.", "options": ["A2a", "A2b"], "answer": 1},
            {"type": "match", "prompt": "A.2-5. Si menziona la sicurezza sul lavoro.", "options": ["A2a", "A2b"], "answer": 0},
            {"type": "match", "prompt": "A.2-6. Si impara una lingua straniera.", "options": ["A2a", "A2b"], "answer": 1},
            {"type": "match", "prompt": "A.2-7. Si citano gli scioperi dei rider.", "options": ["A2a", "A2b"], "answer": 0},
            {"type": "match", "prompt": "A.2-8. L'obiettivo è riqualificarsi.", "options": ["A2a", "A2b"], "answer": 1},
            {"type": "match", "prompt": "A.2-9. Il contesto è la consegna merci in città.", "options": ["A2a", "A2b"], "answer": 0},
            {"type": "match", "prompt": "A.2-10. Il contesto è l'offerta del comune.", "options": ["A2a", "A2b"], "answer": 1},
            {"type": "open", "prompt": "A.3-1. Secondo il testo, cosa deve diventare il giovane nella gig economy?", "ref": "Deve diventare \"imprenditore di se stesso\".", "rows": 2},
            {"type": "open", "prompt": "A.3-2. Quali tre aspetti deve gestire?", "ref": "Deve gestire brand, orari e formazione.", "rows": 2},
            {"type": "open", "prompt": "A.3-3. L'autore definisce questa libertà \"faticosa\": perché?", "ref": "Perché richiede autonomia costante e fatica.", "rows": 2},
            {"type": "open", "prompt": "A.3-4. Qual è, secondo l'autore, un lato positivo?", "ref": "È una scuola di autonomia.", "rows": 2},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "B.1 — Saggio breve / esperienza（二选一，120–180 词）",
             "prompt": "Scegli UNO: (a) Racconta la tua esperienza con un lavoro flessibile o digitale (gig economy, freelance, consegne…): cosa hai imparato? (b) Argomenta: «La formazione continua è oggi più importante del titolo di studio.» Sei d'accordo? Perché?",
             "limit": "120–180 词",
             "reference":
"""Sono convinto che oggi la formazione continua conti più del titolo di studio. Il mondo cambia rapidamente: professioni che esistevano dieci anni fa sono scomparse, mentre ne nascono di nuove legate al digitale. Un diploma o una laurea garantiscono una base, ma non bastano per tutta la carriera. Chi impara a imparare resta competitivo; chi si ferma rischia l'obsolescenza. Certo, il titolo apre porte all'inizio, ma sono le competenze aggiornate a tenerle aperte. Penso ad amici rider che, frequentando corsi serali, hanno cambiato vita. Tuttavia serve equità: la formazione non deve essere un lusso per pochi. In conclusione, il titolo è un punto di partenza, la formazione continua è la vera benzina del lavoro moderno."""},
            {"title": "B.2 — Lettera / e-mail（三选一，80–100 词）",
             "prompt": "Scegli UNO: (a) Scrivi a un'amica che vuole fare la rider: dalle un consiglio. (b) Scrivi all'ufficio risorse umane: chiedi informazioni su un corso di formazione aziendale. (c) Scrivi a un collega: esprimi la tua opinione sullo smart working nella vostra azienda.",
             "limit": "80–100 词",
             "reference":
"""Cara Giulia, so che vuoi fare la rider quest'estate. Ti scrivo per darti un consiglio onesto: il lavoro è flessibile e guadagni subito, ma attenzione alla precarietà. Non avrai contratto, ferie né malattia, e l'algoritmo deciderà i tuoi turni. Usa sempre il casco e rispetta il traffico, perché gli incidenti sono frequenti. Se puoi, frequenta nel tempo libero un corso di formazione: ti aiuterà a trovare qualcosa di più stabile. Un abbraccio, Marco."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""Lo smart working _____ (1) diffuso durante la pandemia ed _____ (2) rimasto una consuetudine per molte aziende. Chi lavora _____ (3) casa risparmia tempo _____ (4) spostamenti e _____ (5) dedica alle proprie passioni. Tuttavia il confine tra vita _____ (6) lavoro diventa più sottile, poiché il dipendente _____ (7) connette anche la sera _____ (8) nei weekend. I sindacati chiedono regole chiare, _____ (9) il diritto _____ (10) staccare va garantito. Per _____ (11) motivo alcune imprese hanno firmato _____ (12) accordi sul diritto alla disconnessione.

La gig economy _____ (13) cambiato il mondo del lavoro. Oggi milioni di persone _____ (14) grazie a piattaforme digitali, _____ (15) i loro diritti sono spesso limitati. Un rider _____ (16) lavora senza contratto non _____ (17) malattia né ferie. Per _____ (18) motivo i sindacati chiedono tutele maggiori. La formazione _____ (19) aiuta a restare competitivi, _____ (20) richiede tempo _____ (21) denaro. Chi _____ (22) forma ha più probabilità di trovare occupazione stabile. _____ (23) tutti possono permettersi di studiare.""",
            "answers": ["è","è","a","negli","lo","e","si","e","perché","di","questo","degli","ha","lavorano","ma","che","ha","questo","ci","ma","e","si","Tuttavia"]},
         "rewrite": [
            {"prompt": "1. Studio la sera. Sono stanco. Voglio migliorare.", "ref": "Studio la sera perché, pur essendo stanco, voglio migliorare."},
            {"prompt": "2. Il corso è online. È gratuito. Mi iscrivo.", "ref": "Poiché il corso è online e gratuito, mi iscrivo."},
            {"prompt": "3. Lei ha figli. Lavora da casa. Concilia meglio.", "ref": "Lei, avendo figli e lavorando da casa, concilia meglio la vita con il lavoro."},
            {"prompt": "4. L'azienda offre formazione. I dipendenti sono felici. La produttività sale.", "ref": "L'azienda offre formazione, perciò i dipendenti sono felici e la produttività sale."},
            {"prompt": "5. Il lavoro è precario. I giovani soffrono. Lo Stato deve intervenire.", "ref": "Poiché il lavoro è precario e i giovani soffrono, lo Stato deve intervenire."},
            {"prompt": "6. Ho fatto un corso. Ho trovato lavoro. Sono contento.", "ref": "Avendo fatto un corso, ho trovato lavoro e sono contento."},
            {"prompt": "7. Lui guadagna poco. Fa due lavori. È sempre stanco.", "ref": "Lui guadagna poco, fa due lavori e perciò è sempre stanco."},
         ],
         "wordform": [
            {"text": "1. Se _____ (potere) studiare, lo farei volentieri.", "answers": ["potessi"]},
            {"text": "2. È importante che i rider _____ (avere) una tutela.", "answers": ["abbiano"]},
            {"text": "3. Senza la formazione, sarebbe difficile _____ (trovare) lavoro.", "answers": ["trovare"]},
            {"text": "4. Il corso _____ (frequentare) da molti giovani quest'anno.", "answers": ["è frequentato"]},
            {"text": "5. Più si _____ (formarsi), più si _____ (guadagnare).", "answers": ["si forma","guadagna"]},
            {"text": "6. Spero che tu _____ (riuscire) a conciliare vita e lavoro.", "answers": ["riesca"]},
            {"text": "7. _____ (noi / continuare) a formarci anche dopo la laurea.", "answers": ["Continuiamo"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "D.1-1. La gig economy è fatta di：", "options": ["A) contratti fissi", "B) micro-incarichi", "C) pensioni"], "answer": 1},
            {"type": "mc", "prompt": "D.1-2. Vantaggio principale：", "options": ["A) stipendio alto", "B) flessibilità", "C) ferie"], "answer": 1},
            {"type": "mc", "prompt": "D.1-3. Svantaggio principale：", "options": ["A) precarietà", "B) noia", "C) viaggi"], "answer": 0},
            {"type": "mc", "prompt": "D.1-4. I rider hanno：", "options": ["A) contratto", "B) no, non ce l'hanno", "C) casa"], "answer": 1},
            {"type": "mc", "prompt": "D.1-5. La formazione serve ma：", "options": ["A) è inutile", "B) va resa pubblica", "C) costa poco"], "answer": 1},
            {"type": "mc", "prompt": "D.1-6. La scuola serale è a：", "options": ["A) Roma", "B) Milano", "C) Napoli"], "answer": 1},
            {"type": "mc", "prompt": "D.1-7. Si chiama：", "options": ["A) Ruota della conoscenza", "B) Scuola dei rider", "C) Corso lavoro"], "answer": 0},
            {"type": "mc", "prompt": "D.1-8. I corsi sono：", "options": ["A) a pagamento", "B) gratuiti", "C) solo online"], "answer": 1},
            {"type": "mc", "prompt": "D.1-9. Chi li finanzia?", "options": ["A) privati", "B) il comune", "C) l'UE"], "answer": 1},
            {"type": "mc", "prompt": "D.1-10. Iscritti nel primo mese：", "options": ["A) 50", "B) 100", "C) 200"], "answer": 1},
            {"type": "cloze", "text": "D.2-1. Fa la rider da _____ anni.", "answers": ["due"]},
            {"type": "cloze", "text": "D.2-2. All'inizio _____ gli orari.", "answers": ["scelgo"]},
            {"type": "cloze", "text": "D.2-3. Non ha _____ né malattia.", "answers": ["ferie"]},
            {"type": "cloze", "text": "D.2-4. Studia di _____ per cambiare vita.", "answers": ["notte"]},
            {"type": "cloze", "text": "D.2-5. Sogna un lavoro con un _____.", "answers": ["contratto"]},
            {"type": "cloze", "text": "D.2-6. Ha fatto un corso di _____.", "answers": ["contabilità"]},
            {"type": "cloze", "text": "D.2-7. Ora _____ CV alle aziende.", "answers": ["invio"]},
            {"type": "cloze", "text": "D.2-8. Secondo lui, trovare lavoro è _____.", "answers": ["difficile"]},
            {"type": "cloze", "text": "D.2-9. Lui non _____ (non si arrende).", "answers": ["molla"]},
            {"type": "cloze", "text": "D.2-10. Il tema del testo è _____ e formazione.", "answers": ["gig economy / rider"]},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 描述图片并回答；② 概述短文并回答；③ 情境角色扮演。
任务：① 描述一张 "un rider davanti a un ristorante con uno zaino" 的图片，并回答 "Secondo te, questo lavoro è libero o precario?"；② 读关于 "corso serale per rider" 的短文，做 2–3 句概述，并回答 "La formazione basta a risolvere la precarietà?"；③ 角色扮演：Sei un sindacalista；考官（datore di lavoro）说 "I rider sono liberi professionisti." 你用论证反驳其权利。""",
             "points": 50,
             "rubric":
"""① 描述图片准确，能用 libero / precario 等 B2 词汇表达评判；② 能做 2–3 句 riassunto 且回答有个人立场；③ 角色扮演用 congiuntivo / passivo 论证；④ 整体语域恰当、连接自然、语法错误不影响理解。""",
             "dims": [
                ("Pronuncia 发音", "发音标准，语域与场合匹配"),
                ("Fluenza 流利度", "表达连贯，能展开论述与评论"),
                ("Grammatica 语法", "虚拟 / 条件 / 关系代词较准确"),
                ("Contenuto 内容", "概述完整、立场清晰，论证有逻辑"),
                ("Interazione 互动", "听证会 / 角色扮演说服力强，论证权利"),
             ],
             "ref":
"""Nella figura vedo un rider davanti a un ristorante con uno zaino sulle spalle. Aspetta una consegna, è in piedi sul marciapiede e controlla il telefono. È un lavoro che sembra libero, perché sceglie gli orari, ma in realtà è precario: non ha contratto, né ferie, né malattia. Il testo parla di una scuola serale per rider, la "Ruota della conoscenza" a Milano: corsi gratuiti di informatica e italiano finanziati dal comune, con cento iscritti nel primo mese. A mio parere la formazione non basta da sola a risolvere la precarietà, perché senza diritti il problema resta. La formazione aiuta, ma servono tutele vere. Signor datore di lavoro, Lei dice che i rider sono liberi professionisti, ma non è così: sono lavoratori subordinati, perché l'algoritmo decide turni e paga. Chiediamo un contratto e la rappresentanza sindacale."""},
         ]},
    ],
})

# ============================== C1 =========================================
LEVELS.append({
    "code": "C1", "name": "CELI 4",
    "subtitle": "il futuro del lavoro / diritti dei lavoratori",
    "theme": "💼 Lavoro, occupazione e carriera", "subj_max": 50,
    "audio": [
        {"title": "Intervista — Sociologa del lavoro", "body":
"""Il futuro del lavoro non è una questione tecnica, ma politica. L'automazione porterà benefici solo se accompagnata da diritti. Oggi il 23% dei lavoratori europei è in una forma di precarietà. Servono tre cose: formazione permanente, un reddito ponte durante la transizione, e rappresentanza sindacale negli algoritmi. Altrimenti, rischiamo una società a due velocità. La mia proposta: un'ora di lavoro su cinque dovrebbe essere dedicata all'apprendimento. Non è utopia, è sopravvivenza."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo 1 — Articolo accademico（il futuro del lavoro）", "body":
"""Le previsioni dell'ILO indicano che entro il 2030 l'automazione sostituirà circa il 9% dei posti di lavoro nei paesi OCSE, ma ne creerà altrettanti in settori oggi inesistenti. La transizione, tuttavia, non sarà indolore: colpirà soprattutto mansioni ripetitive e lavoratori a bassa qualifica. Il vero nodo non è la quantità di posti, ma la qualità e la distribuzione. Senza politiche attive, il divario tra chi possiede le competenze digitali e chi ne è escluso rischia di diventare un abisso."""},
            {"title": "Testo 2 — Intervento opinionista（diritti dei lavoratori）", "body":
"""Mentre i tecnocrati celebrano la "fine del lavoro", resta un silenzio imbarazzante sui diritti. L'automazione non libera l'umanità: semplicemente sposta il valore verso chi possiede gli algoritmi. I lavoratori della gig economy, già oggi, producono ricchezza senza tutele. Invocare il futuro per giustificare la precarietà presente è una retorica comoda. Se vogliamo un futuro davvero umano, i diritti non possono essere un optional della transizione."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Secondo l'ILO, entro il 2030 l'automazione：", "options": ["A) elimina tutti i posti", "B) sostituisce il 9%, ma ne crea altrettanti", "C) non cambia nulla"], "answer": 1},
            {"type": "mc", "prompt": "2. La transizione colpirà soprattutto：", "options": ["A) i manager", "B) mansioni ripetitive e bassa qualifica", "C) gli artisti"], "answer": 1},
            {"type": "mc", "prompt": "3. Il \"vero nodo\" citato è：", "options": ["A) il numero di posti", "B) qualità e distribuzione", "C) il clima"], "answer": 1},
            {"type": "mc", "prompt": "4. Il tono del Testo 2 è：", "options": ["A) neutrale", "B) critico / polemico", "C) pubblicitario"], "answer": 1},
            {"type": "mc", "prompt": "5. L'opinionista definisce \"rettorica comoda\"：", "options": ["A) la formazione", "B) giustificare la precarietà col futuro", "C) il sindacato"], "answer": 1},
            {"type": "mc", "prompt": "6. Entrambi i testi concordano sul fatto che：", "options": ["A) il futuro è roseo", "B) servono politiche / tutele", "C) il lavoro finirà"], "answer": 1},
            {"type": "tf", "prompt": "7. L'automazione creerà solo posti peggiori.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "8. Il divario digitale è una preoccupazione del Testo 1.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "9. Il Testo 2 sostiene che l'automazione libera l'umanità.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "10. I gig worker producono ricchezza senza tutele, per il Testo 2.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "11. I due testi hanno posizioni identiche su tutto.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "12. Per l'opinionista, i diritti devono essere centrali nella transizione.", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito (a) — Riassunto（摘要，80–100 词）",
             "prompt": "Sintetizza le due posizioni dei testi letti in italiano corretto (tono accademico vs polemico, automazione e diritti).",
             "limit": "80–100 词",
             "reference":
"""Il Testo 1, di tono accademico, prevede che entro il 2030 l'automazione sostituirà il 9% dei posti nei paesi OCSE ma ne creerà altrettanti; il rischio reale è la qualità e la distribuzione, con un divario digitale crescente. Il Testo 2, polemico, denuncia che l'entusiasmo per il "fine del lavoro" ignora i diritti: la ricchezza migra verso chi possiede gli algoritmi, mentre i gig worker restano senza tutele. Entrambi convengono che servono politiche attive e tutele, pena una transizione ingiusta."""},
            {"title": "Compito (b) — Saggio / articolo（议论文，150–180 词）",
             "prompt": "\"Il futuro del lavoro sarà giusto solo se i diritti accompagnano l'automazione.\" Sviluppa la tua tesi con argomenti e un esempio.",
             "limit": "150–180 词",
             "reference":
"""Il futuro del lavoro sarà giusto solo se i diritti accompagnano l'automazione. Non basta celebrare l'efficienza delle macchine: occorre garantire che nessuno resti indietro. Come osserva il Testo 1, il problema non è il numero di posti, ma la loro qualità e distribuzione. Se la transizione è lasciata al mercato, il divario tra chi possiede le competenze digitali e chi ne è escluso diventerà un abisso. A mio avviso, i diritti — contratto, formazione, rappresentanza — devono precedere il profitto, non seguirlo. Un esempio concreto: riconoscere ai rider lo status di lavoratori subordinati, con tutele e sindacato, eviterebbe sfruttamento mascherato da "libertà". In conclusione, l'automazione può essere un'opportunità solo se incatenata al rispetto della persona."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""La transizione digitale _____ (1) nuove competenze che _____ (2) lavoratori devono acquisire. Chi non _____ (3) adatta rischia l'esclusione dal mercato. È _____ (4) una rete di sicurezza che tuteli i diritti. I diritti _____ (5) essere garantiti per legge e _____ (6) welfare adeguato _____ (7) ridurre le disuguaglianze. Tuttavia, _____ (8) i corsi siano utili, non _____ (9) sufficienti da soli. Serve _____ (10) patto sociale tra Stato e imprese. Se lo Stato non _____ (11) interverrà, il divario _____ (12) allargherà.

L'automazione _____ (13) i posti di lavoro in settori ripetitivi, _____ (14) nuove professioni legate al digitale. Il vero problema non _____ (15) la quantità, ma la qualità e _____ (16) distribuzione. Senza politiche attive, il divario tra chi _____ (17) le competenze digitali e chi ne _____ (18) escluso rischia _____ (19) diventare un abisso. I sindacati chiedono _____ (20) i lavoratori siano rappresentati negli algoritmi. È giusto che _____ (21) diritti precedano il profitto, non _____ (22) seguano. Solo _____ (23) questa condizione la transizione sarà giusta.""",
            "answers": ["richiede","i","si","necessaria","devono","e","può","benché","sono","un","interverrà","si","sostituisce","crea","è","la","possiede","è","di","che","i","lo","a"]},
         "rewrite": [
            {"prompt": "1. L'automazione sostituisce i posti ripetitivi. Crea nuove professioni digitali. Il mercato cambia.", "ref": "L'automazione, sostituendo i posti ripetitivi e creando nuove professioni digitali, sta cambiando il mercato."},
            {"prompt": "2. I diritti sono limitati. I gig worker protestano. Lo Stato deve intervenire.", "ref": "Poiché i diritti sono limitati e i gig worker protestano, lo Stato deve intervenire."},
            {"prompt": "3. Il corso è gratuito. È online. Mi iscrivo subito.", "ref": "Siccome il corso è gratuito e online, mi iscrivo subito."},
            {"prompt": "4. Lei ha figli. Lavora da casa. Concilia meglio vita e lavoro.", "ref": "Lei, avendo figli e lavorando da casa, concilia meglio vita e lavoro."},
            {"prompt": "5. L'azienda offre formazione. I dipendenti sono felici. La produttività sale.", "ref": "L'azienda offre formazione, perciò i dipendenti sono felici e la produttività sale."},
            {"prompt": "6. Il lavoro è precario. I giovani soffrono. Occorre una rete di sicurezza.", "ref": "Poiché il lavoro è precario e i giovani soffrono, occorre una rete di sicurezza."},
            {"prompt": "7. Tu impari a programmare. Io ti aiuto. Riuscirai a trovare lavoro.", "ref": "Se tu impari a programmare, io ti aiuterò e riuscirai a trovare lavoro."},
         ],
         "wordform": [
            {"text": "1. Sarebbe giusto che tutti _____ (potere) formarsi.", "answers": ["potessero"]},
            {"text": "2. Senza intervento pubblico, la precarietà _____ (aumentare, condizionale).", "answers": ["aumenterebbe"]},
            {"text": "3. I diritti _____ (riconoscere, passivo) dalla legge.", "answers": ["sono riconosciuti"]},
            {"text": "4. È il sindacato _____ (che / cui / a cui) difende i lavoratori.", "answers": ["che"]},
            {"text": "5. _____ (Malgrado / Malgrado che) le difficoltà, lottiamo.", "answers": ["Malgrado"]},
            {"text": "6. Preferisco che tu _____ (venire) al corso.", "answers": ["venga"]},
            {"text": "7. Se io _____ (avere) più tempo, studierei una nuova professione.", "answers": ["avessi"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "cloze", "text": "Tabella 1. Il _____ % dei lavoratori europei è in una forma di precarietà.", "answers": ["23%"]},
            {"type": "cloze", "text": "Tabella 2. Prima cosa necessaria: la _____.", "answers": ["formazione permanente"]},
            {"type": "cloze", "text": "Tabella 3. Terza cosa: la _____ negli algoritmi.", "answers": ["rappresentanza sindacale"]},
            {"type": "cloze", "text": "Tabella 4. Un'ora di lavoro su cinque dovrebbe essere dedicata all'_____.", "answers": ["apprendimento"]},
            {"type": "tf", "prompt": "5. La sociologa dice che il futuro è solo tecnico.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "6. L'algoritmo va rappresentato sindacalmente.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "7. La proposta di 1 ora su 5 è definita utopia.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "8. Il rischio è una società a due velocità.", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""带材料面试（长篇论述 + 深度讨论）。
Materiale: breve testo sull'automazione e i diritti (vedi Testo 2)。
Task：① Esponi la tua posizione in 2–3 minuti: "L'automazione deve essere subordinata ai diritti umani. Sei d'accordo?"；② Discussione con l'esaminatore: rispondi a obiezioni (es. "Ma l'automazione crea ricchezza") e proponi una misura concreta。""",
             "points": 50,
             "rubric":
"""① 论述结构清晰（tesi → argomenti → esempio），语域 formal / argomentativo；② 熟练使用 congiuntivo, condizionale, passivo, relativo；词汇精准（transizione, precarietà, tutela）；③ 讨论中回应质疑并给具体措施；④ 发音流利。""",
             "dims": [
                ("Pronuncia 发音", "发音精准，语调节奏自如"),
                ("Fluenza 流利度", "长篇论述流畅，衔接自然"),
                ("Grammatica 语法", "虚拟 / 条件 / 被动准确，句式丰富"),
                ("Contenuto 内容", "立场明确，词汇丰富（transizione, precarietà, tutela）"),
                ("Interazione 互动", "深度讨论中回应质疑，逻辑自洽"),
             ],
             "ref":
"""La mia posizione è che l'automazione deve essere subordinata ai diritti umani. Non basta celebrare l'efficienza delle macchine: se la transizione è lasciata al mercato, il divario tra chi possiede le competenze digitali e chi ne è escluso diventerà un abisso. Come osserva il Testo 1, il problema non è il numero di posti, ma la loro qualità e distribuzione. I diritti — contratto, formazione, rappresentanza — devono precedere il profitto, non seguirlo. A chi obietta che l'automazione crea ricchezza, rispondo: sì, ma quella ricchezza migra verso chi possiede gli algoritmi, mentre i gig worker restano senza tutele. Una misura concreta? Riconoscere ai rider lo status di lavoratori subordinati e istituire un reddito ponte durante la transizione, così nessuno resta indietro. Solo incatenando l'automazione al rispetto della persona, la transizione sarà davvero giusta."""},
         ]},
    ],
})

# ============================== C2 =========================================
LEVELS.append({
    "code": "C2", "name": "CELI 5",
    "subtitle": "automazione e società / reddito di base incondizionato",
    "theme": "💼 Lavoro, occupazione e carriera", "subj_max": 50,
    "audio": [
        {"title": "Dibattito — Filosofa ed economista", "body":
"""Filosofa: L'automazione ci spoglia dell'agency; il RBI restituisce soggettività ai corpi inutili al mercato.
Economista: Attenzione: un RBI male calibrato spegne l'incentivo. Ma ha ragione sul tema della distribuzione della rendita algoritmica.
Filosofa: Non è carità, è giustizia strutturale. Se la macchina produce, la rendita è collettiva.
Economista: Allora tassiamo la rendita, non il lavoro. Punto di sintesi: RBI come dividendo civico, non assistenza."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo — Saggio（automazione e società / reddito di base）", "body":
"""C'è un'antica beffa dei maghi di Gutenberg: quando la macchina impara a pensare, l'uomo smette di farlo. Oggi, nell'epoca in cui l'algoritmo decide chi assumere e chi licenziare, la profezia si fa carne. Abbiamo automatizzato il lavoro per comprare tempo, e quel tempo l'abbiamo venduto all'algoritmo stesso. La fabbrica non fuma più, ma il suo fantasma amministra le nostre vite dal cloud.
I detrattori del reddito di base incondizionato lo dipingono come l'elemosina dello Stato ai figli viziandati della postmodernità. È un ritratto grottesco: come se il problema fosse la pigrizia di chi, privato del lavoro, osasse respirare senza permesso. In realtà, il RBI è il riconoscimento che il valore non si genera solo nel tempo di cottura della prestazione, ma nella cura, nell'arte, nel pensiero — attività che il mercato misura col metro sbagliato.
La società post-lavoro non sarà né il paradiso promesso dai tecnoutopisti, né l'abisso temuto dai nostalgici. Sarà ciò che decideremo di essere: una comunità che ridistribuisce la rendita della macchina, o una casta di proprietari di algoritmi sopra un popolo di spettatori. La posta in gioco non è economica. È civile."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. La \"beffa di Gutenberg\" metaforizza：", "options": ["A) la stampa", "B) l'uomo che smette di pensare quando la macchina pensa", "C) la scuola"], "answer": 1},
            {"type": "mc", "prompt": "2. «Il tempo l'abbiamo venduto all'algoritmo» è un esempio di：", "options": ["A) metafora", "B) domanda", "C) elenco"], "answer": 0},
            {"type": "mc", "prompt": "3. Il tono verso i detrattori del RBI è：", "options": ["A) rispettoso", "B) ironico / sarcastico", "C) neutrale"], "answer": 1},
            {"type": "mc", "prompt": "4. «Figli viziandati della postmodernità» è：", "options": ["A) una lode", "B) un'ironia sui critici", "C) una notizia"], "answer": 1},
            {"type": "mc", "prompt": "5. Per l'autore, il valore si genera anche in：", "options": ["A) solo nel lavoro pagato", "B) cura, arte, pensiero", "C) nel denaro"], "answer": 1},
            {"type": "mc", "prompt": "6. «La fabbrica… il suo fantasma amministra le nostre vite dal cloud» significa：", "options": ["A) chiusura industriale", "B) controllo algoritmico invisibile", "C) vacanza"], "answer": 1},
            {"type": "mc", "prompt": "7. La \"posta in gioco\" finale è di natura：", "options": ["A) economica", "B) civile / politica", "C) tecnica"], "answer": 1},
            {"type": "mc", "prompt": "8. La posizione dell'autore sul RBI è：", "options": ["A) contraria", "B) favorevole / difensiva", "C) ignorante"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito 1 — Saggio / articolo（约 200–250 词）",
             "prompt": "\"L'automazione ci renderà liberi o ci trasformerà in spettatori?\" Sviluppa una tesi articolata, con riferimenti a società, diritti e RBI.",
             "limit": "200–250 词",
             "reference":
"""L'automazione ci renderà liberi o ci trasformerà in spettatori? La risposta non è tecnica, è politica. Se accettiamo che il valore risieda esclusivamente nella prestazione mercificata, allora la macchina ci renderà superflui — spettatori di una prosperità altrui. Ma se ridisegniamo il contratto sociale, l'automazione può essere l'emancipazione dal lavoro salariato coatto. Il reddito di base incondizionato non è l'elemosina temuta dai detrattori: è il riconoscimento che cura, arte e pensiero — invisibili al PIL — generano civiltà. La posta in gioco è la soggettività stessa: restituire ai corpi espulsi dal mercato la capacità di decidere della propria vita. Una società che ridistribuisce la rendita della macchina smette di chiedere il permesso di esistere. Non sarà il paradiso dei tecnoutopisti, ma una libertà autentica, faticosa e democratica. La scelta è nostra: comunità o casta."""},
            {"title": "Compito 2 — Appello（breve contributo，60–80 词）",
             "prompt": "Scrivi un \"appello\" ai cittadini per sostenere l'introduzione di un reddito di base incondizionato (tono persuasivo / civico).",
             "limit": "60–80 词",
             "reference":
"""Cittadini, l'ora è questa: esigiamo un reddito di base incondizionato. Non è assistenza, è giustizia. Mentre gli algoritmi producono ricchezza, milioni restano fuori. Rivendichiamo la rendita della macchina come bene comune. Firmate, parlate, votate: la dignità non si chiede, si conquista. La libertà comincia quando nessuno deve vendere il proprio tempo per respirare."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""L'avvento dell'automazione _____ (1) le basi stesse della cittadinanza, poiché chi _____ (2) gli algoritmi detiene un potere _____ (3) precedenti. È _____ (4) che il reddito di base _____ (5) istituito prima che il divario _____ (6) approfondisca. Non si tratta _____ (7) un assistenzialismo, bensì _____ (8) riconoscere la dignità del non-lavoro. La società _____ (9) trarrà giovamento, _____ (10) sia governata democraticamente. _____ (11) la macchina produce, il valore _____ (12) diventa collettivo.

La società post-lavoro non sarà il paradiso promesso _____ (13) tecnoutopisti, né l'abisso temuto _____ (14) nostalgici. Sarà ciò _____ (15) decideremo di essere: una comunità che ridistribuisce la rendita _____ (16) macchina, _____ (17) una casta di proprietari di algoritmi sopra un popolo _____ (18) spettatori. La posta _____ (19) gioco non è economica, _____ (20) civile. _____ (21) la distribuzione sia equa, occorre _____ (22) politiche inclusive. _____ (23) il lavoro non è più centrale, la dignità va ripensata.""",
            "answers": ["sconvolge","possiede","senza","auspicabile","venga","si","di","di","ne","purché","Poiché","dunque","dai","dai","che","della","o","di","in","ma","Affinché","adottare","Poiché"]},
         "rewrite": [
            {"prompt": "1. L'automazione spoglia l'uomo dell'agency. Il RBI restituisce soggettività. I corpi diventano inutili al mercato.", "ref": "L'automazione spoglia l'uomo dell'agency, mentre il RBI restituisce soggettività ai corpi che il mercato giudica inutili."},
            {"prompt": "2. L'economista teme l'incentivo. Un RBI male calibrato spegne l'incentivo. Propone di tassare la rendita.", "ref": "Sebbene l'economista temesse che un RBI male calibrato spegnesse l'incentivo, propose di tassare la rendita anziché il lavoro."},
            {"prompt": "3. La macchina produce ricchezza. La rendita è collettiva. Va ridistribuita.", "ref": "Poiché la macchina produce ricchezza, la rendita, essendo collettiva, va ridistribuita."},
            {"prompt": "4. I detrattori dipingono il RBI. È un'elemosina. In realtà è giustizia.", "ref": "I detrattori dipingono il RBI come un'elemosina, mentre in realtà si tratta di giustizia strutturale."},
            {"prompt": "5. Il lavoro salariato è coatto. L'automazione può emanciparci. Occorre ridisegnare il contratto sociale.", "ref": "Se ridisegniamo il contratto sociale, l'automazione può emanciparci dal lavoro salariato coatto."},
            {"prompt": "6. Non è carità. È giustizia. La rendita va tassata.", "ref": "Non essendo carità, ma giustizia, la rendita va tassata."},
            {"prompt": "7. La società sceglierà. Saremo comunità o casta. Dipende da noi.", "ref": "Che la società sia comunità o casta dipenderà dalla scelta che noi faremo."},
         ],
         "wordform": [
            {"text": "1. _____ (Posto / Posta / Essendo posta) la posta in gioco, agiamo.", "answers": ["Posta"]},
            {"text": "2. Non tanto il lavoro, _____ (quanto / ma / come) la sua distribuzione conta.", "answers": ["quanto"]},
            {"text": "3. Se l'algoritmo decidesse, noi _____ (subire / subiremmo / subiamo).", "answers": ["subiremmo"]},
            {"text": "4. È il tempo _____ (in cui / dove / che) si pensa, non si produce.", "answers": ["in cui"]},
            {"text": "5. _____ (Né / Ne / Non) il paradiso né l'abisso si avvereranno senza scelta.", "answers": ["Né"]},
            {"text": "6. Che _____ (si riconosca / riconosca / si riconosca a) la dignità è essenziale.", "answers": ["si riconosca"]},
            {"text": "7. Il valore non si genera solo nel tempo di _____ (cuocere → cottura) della prestazione.", "answers": ["cottura"]},
            {"text": "8. La _____ (automatizzare → automatizzazione) del lavoro ha ridisegnato il contratto sociale.", "answers": ["automatizzazione"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "1. La filosofa vede il RBI come：", "options": ["A) carità", "B) restituzione di soggettività / giustizia", "C) errore"], "answer": 1},
            {"type": "mc", "prompt": "2. L'economista teme che un RBI sbagliato：", "options": ["A) aiuti troppo", "B) spenga l'incentivo", "C) costi poco"], "answer": 1},
            {"type": "mc", "prompt": "3. Il punto di sintesi è：", "options": ["A) RBI = dividendo civico", "B) abolire il RBI", "C) tassare il lavoro"], "answer": 0},
            {"type": "mc", "prompt": "4. Atteggiamento dell'economista verso la filosofa：", "options": ["A) totale disaccordo", "B) parziale convergenza", "C) indifferenza"], "answer": 1},
            {"type": "mc", "prompt": "5. La \"rendita algoritmica\" va：", "options": ["A) privatizzata", "B) tassata / distribuita", "C) ignorata"], "answer": 1},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""抽象话题（哲学 / 艺术 / 社会伦理）演讲 + 批判性质疑回应。
Tema: "Se la macchina produce, a chi appartiene il valore?"
Task：① Prepara un intervento di 3–4 minuti di tono saggistico；② L'esaminatore ti sottoporrà obiezioni etiche (es. "Il RBI svilisce il lavoro come dignità"). Tu ribatti rigorosamente。""",
             "points": 50,
             "rubric":
"""① 演讲具 saggistica / 哲思语域，善用 metafora, ironia, contrapposizione（comunità vs casta）；② 句法复杂且准确：periodare, congiuntivo, passivo, incisi；词汇高级（agency, rendita, soggettività, paradigma）；③ 承接质疑并以 rigorosa argomentazione 反驳；④ 发音地道、节奏自如。""",
             "dims": [
                ("Pronuncia 发音", "发音精准，学术语域自如"),
                ("Fluenza 流利度", "演讲连贯，抽象概念流转自然"),
                ("Grammatica 语法", "复杂句法准确（虚拟 / 条件 / 被动 / 关系）"),
                ("Contenuto 内容", "抽象概念清晰，词汇精准（agency, rendita, soggettività）"),
                ("Pensiero critico 思辨", "批判性回应质疑，逻辑自洽有深度"),
             ],
             "ref":
"""Se la macchina produce, a chi appartiene il valore? La mia tesi è che il valore generato dall'automazione non appartiene a chi possiede gli algoritmi, ma alla comunità intera, perché nasce da un sapere collettivo e da infrastrutture pubbliche. Quando la macchina impara a pensare, l'uomo non smette di farlo: smette di venderlo. La rendita algoritmica è, per definizione, collettiva, e va ridistribuita come dividendo civico, non come privilegio di pochi. A chi obietta che il reddito di base svilisce il lavoro come dignità, rispondo ribaltando i termini: la dignità non sta nel tempo di cottura della prestazione mercificata, ma nella cura, nell'arte, nel pensiero — attività che il mercato misura col metro sbagliato. Il RBI non è elemosina, è il riconoscimento che il non-lavoro ha valore. Restituire ai corpi espulsi dal mercato la soggettività significa ridisegnare il contratto sociale. La scelta è nostra: comunità che ridistribuisce, o casta di proprietari sopra spettatori."""},
         ]},
    ],
})

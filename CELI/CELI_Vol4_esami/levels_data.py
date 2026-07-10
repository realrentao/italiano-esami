# -*- coding: utf-8 -*-
'''Dati strutturati del Vol.4 (A1-C2) — Tema: Salute, alimentazione e benessere.
Genera 6 pagine d'esame CELI leggibili dal generatore (generator_template.py).
'''
VOL_NO = 4
THEME_EMOJI = "🥗"
THEME_TEXT = "Salute, alimentazione e benessere"

LEVELS = []

# ============================== A1 =========================================
LEVELS.append({
    "code": "A1", "name": "CELI Impatto",
    "subtitle": "sport e salute / frutta e verdura",
    "theme": "🥗 Salute, alimentazione e benessere", "subj_max": 20,
    "audio": [],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo 1 — Avviso（通知）", "body":
'''CENTRO SPORT SALUTE
Corso di nuoto per bambini e adulti.
Lunedì e mercoledì, ore 18.00.
Prezzo: 25 euro al mese.
Vieni con tutta la famiglia!'''},
            {"title": "Testo 2 — Cartolina（明信片）", "body":
'''Cara Giulia,
sono in montagna con la mia famiglia. La mattina faccio passeggiate e faccio sport. Mangi amo tanta frutta e verdura dell'orto: mele, pere e pomodori. È tutto buonissimo! E tu? Fai sport? Un bacio,
Marco'''},
            {"title": "Testo 3 — Pubblicità（广告）", "body":
'''FRUTTA E VERDURA FRESCA
Vieni al mercato di piazza Garibaldi!
Lunedì, mercoledì e sabato, dalle 8 alle 13.
Mele, arance, carote e insalata a buon prezzo.'''},
         ],
         "items": [
            {"type": "match", "prompt": "1. Il Testo 1 è：", "options": ["A) un avviso", "B) una cartolina", "C) una pubblicità"], "answer": 0},
            {"type": "match", "prompt": "2. Il Testo 2 è：", "options": ["A) un avviso", "B) una cartolina", "C) una pubblicità"], "answer": 1},
            {"type": "match", "prompt": "3. Il Testo 3 è：", "options": ["A) un avviso", "B) una cartolina", "C) una pubblicità"], "answer": 2},
            {"type": "mc", "prompt": "4. Il corso di nuoto è：", "options": ["A) solo per bambini", "B) per bambini e adulti", "C) solo di domenica"], "answer": 1},
            {"type": "mc", "prompt": "5. Marco mangia：", "options": ["A) solo dolci", "B) frutta e verdura dell'orto", "C) al ristorante"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Scrivi una cartolina（明信片 / 留言）",
             "prompt": "Scrivi una cartolina a un tuo amico/a. Parla di due cose: fai sport? mangi frutta e verdura? Scrivi 2–3 frasi（30–50 parole）。Usa il presente. Inizia con \"Ciao [nome]!\" e firma in fondo.",
             "limit": "30–50 词",
             "reference":
'''Ciao Paolo! Faccio sport ogni giorno: vado in bicicletta e gioco a calcio. Mangi o frutta e verdura? Io mangio mele e pomodori dell'orto. Fare sport fa bene alla salute! Un abbraccio, Marco.'''},
         ]},
        {"kind": "oral", "title": "3. Prova orale（口语，含听力评定）",
         "tasks": [
            {"desc":
'''CELI A1 无独立听力卷，听力并入口语评定。考官先念 1–2 句极简单指示（模拟音频文本），考生听懂并回应，再进入引导问答与简单表达。
① 考官朗读："Buongiorno. Come ti chiami?" / "Che cosa fai per stare in salute?" / "Mangi frutta e verdura?"
② 引导问答：1. Come ti chiami? / Quanti anni hai? 2. Dove abiti? 3. Fai sport? Quale? 4. Mangi frutta e verdura ogni giorno? 5. Che cosa mangi a colazione?
③ 简单表达：用 2–3 句介绍自己典型一天里「健康的事」（"La mattina faccio sport.", "Mangio una mela."）。''',
             "points": 20,
             "rubric":
'''① 能听懂考官朗读的 1–2 句简单指示并作出回应（听力并入）；② 问答切题，使用 presente semplice 基本正确；③ 发音可懂，词汇为基础级（sport, frutta, salute, casa 等）；④ 能说出 2–3 句连贯自我介绍 / 健康习惯。''',
             "dims": [
                ("Pronuncia 发音", "单音基本准确，语调自然，能听懂简单指令"),
                ("Fluenza 流利度", "能用基本词汇与单句作答，无明显长时间停顿"),
                ("Grammatica 语法", "使用基础句型（essere/avere/ presente），错误不影响理解"),
                ("Contenuto 内容", "覆盖姓名 / 年龄 / 住址 / 健康习惯等任务要求"),
                ("Interazione 互动", "能回应考官提问，维持简短交流"),
             ],
             "ref":
'''Buongiorno, mi chiamo Marco e ho dodici anni. Abito a Bologna con i miei genitori. Per stare in salute faccio sport ogni giorno: la mattina vado in bicicletta e gioco a calcio con i miei amici. Mangio tanta frutta e verdura, per esempio mele e pomodori dell'orto. La sera mangio un'insalata e bevo acqua. Non mangio molti dolci. Fare sport e mangiare bene mi fa sentire forte e felice. E tu, fai sport?'''},
         ]},
    ],
})

# ============================== A2 =========================================
LEVELS.append({
    "code": "A2", "name": "CELI 1",
    "subtitle": "una dieta equilibrata / andare dal medico",
    "theme": "🥗 Salute, alimentazione e benessere", "subj_max": 30,
    "audio": [
        {"title": "Testo 1 — Dialogo（andare dal medico）", "body":
'''Dottore: Buongiorno, che cosa ha?
Paziente: Ho mal di testa e un po' di febbre.
Dottore: Da quanto tempo?
Paziente: Da due giorni.
Dottore: Prenda questa medicina due volte al giorno e riposi. Beva molta acqua.'''},
        {"title": "Testo 2 — Annuncio（cibo sano）", "body":
'''Vuoi mangiare sano? Da "Cucina Verde" prepariamo pasti equilibrati con verdure fresche. Consegna a domicilio il lunedì e il giovedì. Un pasto costa 8 euro. Chiama il 345 678 9012!'''},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，权重 25%）",
         "texts": [
            {"title": "Testo A — Consigli（均衡饮食建议，博客短文）", "body":
'''UNA DIETA EQUILIBRATA
Per stare bene, ho cambiato alimentazione. La mattina mangio cereali e frutta. A pranzo mangio pasta, verdure e un po' di carne o pesce. La sera mangio un'insalata. Bevo due litri di acqua al giorno e non mangio molti dolci. Il medico mi ha detto: "Mangia di tutto, ma con moderazione". Ora mi sento meglio e ho più energia.'''},
            {"title": "Testo B — Appuntamento（看医生，诊所便条）", "body":
'''APPUNTAMENTO DAL MEDICO
La signora Rossi ha chiamato il dottor Bianchi perché aveva mal di gola e febbre. La segreteria ha dato un appuntamento per martedì alle 10.30. Il medico visita in via Roma 12. Portare la tessera sanitaria. Se non può venire, chiamare il 06 123456.'''},
         ],
         "items": [
            {"type": "match", "prompt": "1. Per stare bene, la persona ha cambiato alimentazione. →", "options": ["A", "B"], "answer": 0},
            {"type": "match", "prompt": "2. Una donna ha mal di gola e febbre. →", "options": ["A", "B"], "answer": 1},
            {"type": "match", "prompt": "3. L'appuntamento è di martedì alle 10.30. →", "options": ["A", "B"], "answer": 1},
            {"type": "mc", "prompt": "4. La mattina l'autore mangia：", "options": ["A) pizza", "B) cereali e frutta", "C) solo carne"], "answer": 1},
            {"type": "mc", "prompt": "5. La sera mangia：", "options": ["A) un'insalata", "B) pasta e carne", "C) dolci"], "answer": 0},
            {"type": "mc", "prompt": "6. La signora Rossi ha：", "options": ["A) mal di gola e febbre", "B) solo fame", "C) sonno"], "answer": 0},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 15%）",
         "tasks": [
            {"title": "Compito 1 — Completamenti（补全短文，5 空）",
             "prompt": "La settimana scorsa ho deciso di ________ (1) una dieta più sana. Ho ________ (2) di mangiare più frutta e ho ________ (3) a fare due pasti leggeri la sera. Quando ho avuto mal di testa, sono ________ (4) dal medico. Ora sto meglio e ho più ________ (5).",
             "limit": "填空",
             "reference": "(1) seguire / iniziare；(2) decisio / cercato；(3) cominciato；(4) andato；(5) energia"},
            {"title": "Compito 2 — Espansione（扩写，50–80 词）",
             "prompt": "Espandi il biglietto seguente in un breve messaggio a un amico（50–80 parole）：\"Ciao Sara, non sto bene. Sono andata dal medico ieri. Scrivimi presto!\"",
             "limit": "50–80 词",
             "reference":
'''Ciao Sara, non sto bene. Ieri sono andata dal medico perché avevo mal di gola e un po' di febbre. Il dottore mi ha detto di riposare, bere molta acqua e prendere una medicina due volte al giorno. Ora sto un po' meglio, ma resto a casa. Mangio più frutta e verdura per guarire presto. Scrivimi presto! Un bacio, Lucia.'''},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力，权重 30%）",
         "items": [
            {"type": "match", "prompt": "1. Nel Testo 1, il paziente ha：", "options": ["A) mal di testa e febbre", "B) fame", "C) sonno"], "answer": 0},
            {"type": "match", "prompt": "2. Nel Testo 2, la consegna è：", "options": ["A) lunedì e giovedì", "B) ogni giorno", "C) solo sabato"], "answer": 0},
            {"type": "match", "prompt": "3. Nel Testo 2, il numero di telefono è：", "options": ["A) 06 123456", "B) 345 678 9012", "C) 347 987 6543"], "answer": 1},
            {"type": "mc", "prompt": "4. Il medico dice di prendere la medicina：", "options": ["A) una volta", "B) due volte al giorno", "C) mai"], "answer": 1},
            {"type": "mc", "prompt": "5. Il medico consiglia di：", "options": ["A) correre", "B) riposare e bere acqua", "C) mangiare dolci"], "answer": 1},
            {"type": "mc", "prompt": "6. Un pasto da \"Cucina Verde\" costa：", "options": ["A) 5 euro", "B) 8 euro", "C) 12 euro"], "answer": 1},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语，10min）",
         "tasks": [
            {"desc":
'''① 自我介绍 + 习惯爱好；② 描述图片；③ 角色扮演。
任务：① 介绍自己并说一种健康食物或喜欢的运动；② 描述图片：一家人在市场买果蔬，有苹果、胡萝卜、橙子；③ 角色扮演：你是病人，向考官（医生）说明：喉咙痛 / 发烧 / 睡不好。''',
             "points": 30,
             "rubric":
'''① 自我介绍含 1–2 个习惯 / 爱好（cibo sano, sport），presente 与 passato prossimo 基本正确；② 图片描述能点出人物、食物、动作（compra, ci sono）；③ 角色扮演能用 "Ho mal di…", "Non sto bene" 等基础就医表达；④ 发音清晰、交流自然。''',
             "dims": [
                ("Pronuncia 发音", "发音清晰，重音基本正确"),
                ("Fluenza 流利度", "自我介绍流畅，含个人习惯"),
                ("Grammatica 语法", "现在时 / 近过去时使用基本正确"),
                ("Contenuto 内容", "涵盖自我介绍、图片描述、角色扮演三项任务"),
                ("Interazione 互动", "角色扮演用语得体，完成信息询问"),
             ],
             "ref":
'''Buongiorno, mi chiamo Lucia, ho vent'anni e studio a Firenze. Per stare in salute mangio tanta frutta e verdura ogni giorno e faccio yoga due volte a settimana. Nella foto vedo una famiglia al mercato: la mamma compra mele, carote e arance fresche. Ci sono tante verdure buone! Buongiorno dottore, non sto bene: ho mal di gola, un po' di febbre e ho dormito poco questa notte. Può darmi un consiglio? Grazie.'''},
         ]},
    ],
})

# ============================== B1 =========================================
LEVELS.append({
    "code": "B1", "name": "CELI 2",
    "subtitle": "benessere mentale / fare attività fisica",
    "theme": "🥗 Salute, alimentazione e benessere", "subj_max": 30,
    "audio": [
        {"title": "Testo 1 — Intervista（sport e umore）", "body":
'''Giornalista: Professore, lo sport aiuta davvero la mente?
Psicologo: Sì. Chi fa attività fisica tre volte a settimana ha meno ansia e dorme meglio. Bastano 30 minuti al giorno.
Giornalista: Anche camminare?
Psicologo: Certo, l'importante è muoversi con regolarità, non eccellere.'''},
        {"title": "Testo 2 — Monologo（la mia esperienza）", "body":
'''Io l'anno scorso stavo male per lo stress. Poi ho iniziato lo yoga due volte a settimana. Dopo un mese mi sentivo più calmo e dormivo meglio. Ora esco anche a camminare la domenica con gli amici. Il segreto? Costanza, non perfezione.'''},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，权重 25%）",
         "texts": [
            {"title": "Testo — Articolo del blog（心理健康与体育锻炼）", "body":
'''FARE MOVIMENTO FA BENE ALLA MENTE
Negli ultimi anni ho capito che la salute mentale è importante quanto quella fisica. Quando sono stressato per lo studio o per il lavoro, vado a correre nel parco vicino a casa. Dopo mezz'ora di corsa mi sento più calmo e riesco a pensare meglio. Anche i miei amici dicono che fare attività fisica regolare li aiuta a dormire e a essere di buon umore.
Secondo un'indagine, le persone che fanno sport tre volte a settimana soffrono meno di ansia. Naturalmente, l'attività fisica non risolve tutto: a volte serve parlare con qualcuno o chiedere aiuto a un esperto. Però muoversi è un ottimo inizio. Il mio consiglio è semplice: trova un'attività che ti piace, anche solo una passeggiata, e falla ogni giorno.'''},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Per l'autore, la salute mentale è：", "options": ["A) meno importante", "B) importante quanto quella fisica", "C) inutile"], "answer": 1},
            {"type": "mc", "prompt": "2. Quando è stressato, l'autore：", "options": ["A) dorme tutto il giorno", "B) va a correre", "C) mangia dolci"], "answer": 1},
            {"type": "mc", "prompt": "3. L'indagine dice che chi fa sport 3 volte a settimana：", "options": ["A) soffre di più ansia", "B) soffre meno di ansia", "C) non cambia nulla"], "answer": 1},
            {"type": "mc", "prompt": "4. Il consiglio finale è：", "options": ["A) non muoverti", "B) trova un'attività che ti piace e falla ogni giorno", "C) solo correre"], "answer": 1},
            {"type": "match", "prompt": "5. \"Dopo mezz'ora di corsa mi sento più calmo.\" → beneficio sulla", "options": ["calma", "sonno"], "answer": 0},
            {"type": "match", "prompt": "6. \"L'attività fisica regolare aiuta a dormire e a essere di buon umore.\" → beneficio su", "options": ["umore", "fame"], "answer": 0},
            {"type": "cloze", "text": "7. Secondo il testo, per la salute mentale a volte serve anche ________.", "answers": ["parlare con qualcuno / chiedere aiuto a un esperto"]},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 25%）",
         "tasks": [
            {"title": "Compito 1 — Questionario sul benessere（填问卷，约 60–80 词）",
             "prompt": "Questionario sul benessere — Nome: ___ Età: ___ Fai attività fisica? □ Sì □ No Quante volte a settimana? ___ Che cosa fai per il benessere mentale? Come ti senti oggi?（bene / così così / stanco）",
             "limit": "60–80 词",
             "reference":
'''Nome: Davide  Età: 22
Fai attività fisica? Sì — 3 volte a settimana.
Per il benessere mentale: vado a correre tre volte a settimana e ascolto musica quando studio. La domenica esco con gli amici, così non penso al lavoro. Parlo anche con mia sorella quando sono triste. Mi sento bene perché dormo otto ore.
Come ti senti oggi? bene'''},
            {"title": "Compito 2 — E-mail（叙述过去事件，120–150 词）",
             "prompt": "Scrivi un'email a un amico / un'amica. Racconta come hai migliorato il tuo benessere mentale grazie all'attività fisica（cosa facevi prima, cosa fai adesso, che effetti hai notato）。Usa il passato prossimo e l'imperfetto.",
             "limit": "120–150 词",
             "reference":
'''Ciao Marco, ti scrivo perché ho fatto un cambiamento importante. Un anno fa stavo sempre stanco e un po' triste: passavo le serate sul divano e non uscivo mai. Poi ho cominciato ad andare in palestra due volte alla settimana e a fare lunghe passeggiate nel fine settimana. All'inizio ero molto pigro, ma dopo un mese mi sentivo già più calmo e dormivo meglio. Oggi faccio attività fisica con regolarità e ho notato meno ansia prima degli esami. Per me muoversi è diventato un modo per stare bene con la testa, non solo col corpo. Ti consiglio di provare! Un abbraccio, Davide.'''},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力，权重 25%）",
         "items": [
            {"type": "mc", "prompt": "1. Lo psicologo dice che chi fa sport 3 volte a settimana：", "options": ["A) ha più ansia", "B) ha meno ansia e dorme meglio", "C) non cambia"], "answer": 1},
            {"type": "mc", "prompt": "2. Quanti minuti al giorno bastano？", "options": ["A) 10", "B) 30", "C) 60"], "answer": 1},
            {"type": "mc", "prompt": "3. Anche camminare：", "options": ["A) non conta", "B) conta, l'importante è muoversi", "C) fa male"], "answer": 1},
            {"type": "mc", "prompt": "4. Il protagonista del Testo 2 stava male per：", "options": ["A) fame", "B) stress", "C) sonno"], "answer": 1},
            {"type": "mc", "prompt": "5. Ha iniziato：", "options": ["A) il nuoto", "B) lo yoga", "C) il calcio"], "answer": 1},
            {"type": "cloze", "text": "6. Dopo un mese si sentiva ________.", "answers": ["più calmo"]},
            {"type": "cloze", "text": "7. Dormiva ________.", "answers": ["meglio"]},
            {"type": "cloze", "text": "8. La domenica esce a ________.", "answers": ["camminare con gli amici"]},
            {"type": "cloze", "text": "9. Il segreto è: ________.", "answers": ["costanza, non perfezione"]},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语，权重 25%）",
         "tasks": [
            {"desc":
'''① 自我介绍 / 兴趣 / 日常；② 描述图片；③ 角色扮演。
任务：① 介绍自己、兴趣以及如何照顾心理健康；② 描述图片：一群人在公园做户外瑜伽，有人闭眼，有人缓缓呼吸，描述氛围；③ 角色扮演：你给压力大的朋友（考官）建议："Non ho tempo per lo sport." 你提出简单可行的方案（如散步）。''',
             "points": 30,
             "rubric":
'''① 自我介绍连贯，含兴趣与健康习惯；presente, passato prossimo, imperfetto 使用正确；② 图片描述能传达氛围（calma, respirare, all'aperto）；③ 角色扮演能给出具体可行建议；④ 交流流畅，能应对追问。''',
             "dims": [
                ("Pronuncia 发音", "发音标准，语调节奏自然"),
                ("Fluenza 流利度", "连贯表达观点与习惯，少停顿"),
                ("Grammatica 语法", "现在时 / 近过去时 / 未完成过去时较准确"),
                ("Contenuto 内容", "观点明确，图片描述准确（calma, respirare）"),
                ("Interazione 互动", "说服性角色扮演，用语得体"),
             ],
             "ref":
'''Buongiorno, mi chiamo Davide, ho ventidue anni e studio all'università. Per il mio benessere mentale vado a correre tre volte a settimana e ascolto musica quando studio; la domenica esco con gli amici e così non penso al lavoro. Nella foto vedo un gruppo di persone che fa yoga all'aperto in un parco: alcuni chiudono gli occhi, altri respirano piano. L'atmosfera è molto calma e rilassata. Sai, non hai tempo per lo sport? Ti propongo una cosa semplice: fai una passeggiata di dieci minuti ogni giorno, per esempio andando a lavoro a piedi. La costanza, non la perfezione, è la chiave!'''},
         ]},
    ],
})

# ============================== B2 =========================================
LEVELS.append({
    "code": "B2", "name": "CELI 3",
    "subtitle": "alimentazione consapevole / qualità del sonno",
    "theme": "🥗 Salute, alimentazione e benessere", "subj_max": 50,
    "audio": [
        {"title": "Testo D1a — Intervista（nutrizionista）", "body":
'''Giornalista: Dott.ssa, cos'è l'alimentazione consapevole?
Nutrizionista: È ascoltare il corpo. Non contiamo calorie, ma facciamo attenzione a quando e come mangiamo. Il problema oggi è la velocità: mangiamo correndo.
Giornalista: Funziona per tutti?
Nutrizionista: Sì, ma serve tempo. Chi inizia vede risultati in tre settimane: più energia, meno gonfiore.'''},
        {"title": "Testo D1b — Servizio（sonno e lavoro）", "body":
'''A Torino un'azienda ha introdotto la "stanza del sonno". I dipendenti possono riposare 20 minuti dopo pranzo. Il risultato: meno errori del 15% e meno malattie. Il fondatore dice: "Chi dorme decide meglio". Cento aziende in Italia ora copiano il modello.'''},
        {"title": "Testo D2 — Monologo", "body":
'''Due anni fa stavo male: mangiavo in modo disordinato e dormivo quattro ore. Poi ho cambiato. Ora mangio seduta, senza telefono, e vado a letto alle 23. Faccio yoga tre volte a settimana. La mattina mi sveglio alle 7 e mi sento in forma. Non è perfetto, ma è mio. Consiglio a tutti di iniziare piano.'''},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，A.1+A.2+A.3）",
         "texts": [
            {"title": "A.1 — Testo A1a（alimentazione consapevole）", "body":
'''L'alimentazione consapevole non è una dieta: è un cambio di relazione col cibo. Significa riconoscere la differenza tra fame fisica e fame emotiva, rallentare a tavola e scegliere cibi che nutrono davvero. Diversi studi mostrano che chi pratica la mindful eating riduce gli episodi di abbuffata e migliora la digestione. Tuttavia, la consapevolezza da sola non basta se il contesto non aiuta: la pubblicità, i prezzi degli alimenti freschi e l'organizzazione del tempo libero condizionano le scelte ben più della buona volontà individuale. Serve perciò una politica alimentare che renda sostenibile il gesto quotidiano di chi vuole mangiare meglio.'''},
            {"title": "A.1 — Testo A1b（qualità del sonno）", "body":
'''Dormire non è un lusso, è una funzione biologica essenziale. Eppure, tra schermi accesi fino a tardi, caffè serali e ritmi di lavoro compressi, la qualità del sonno degli europei è in calo. La privazione cronica di sonno aumenta il rischio di obesità, diabete e disturbi dell'umore. Alcune aziende hanno introdotto "pause di sonno" o orari flessibili per proteggere il riposo dei dipendenti, ottenendo calo di errori e assenteismo. La scienza è chiara: chi dorme bene decide meglio. Recuperare il sonno non richiede tecnologia costosa, ma disciplina e confini netti tra lavoro e riposo.'''},
            {"title": "A.2 — Testo A2a（5 consigli per l'alimentazione）", "body":
'''1. Fai la spesa con una lista, per evitare acquisti impulsivi.
2. Mangi a tavola, senza telefono né televisione.
3. Scegli alimenti freschi e di stagione quando possibile.
4. Ascolta i segnali di sazietà prima di riempire di nuovo il piatto.
5. Prepara i pasti a casa: cucinare è anche un atto di cura.'''},
            {"title": "A.2 — Testo A2b（5 consigli per la qualità del sonno）", "body":
'''6. Spegni gli schermi almeno un'ora prima di dormire.
7. Vai a letto e alzati sempre alla stessa ora.
8. Evita caffè e tè dopo le 16.
9. Mantieni la camera da letto buia e fresca.
10. Non usare il letto per lavorare o guardare serie TV.'''},
            {"title": "A.3 — Testo（alimentazione e sonno）", "body":
'''Quando ho iniziato a cenare due ore prima di dormire e a smettere di mangiare davanti allo schermo, il mio sonno è migliorato in pochi giorni. Non è stata una "dieta", ma un ritorno alla regolarità. Oggi considero alimentazione consapevole e qualità del sonno due facce della stessa medaglia: entrambe richiedono attenzione, lentezza e il coraggio di dire no a ciò che ci distrae. La salute, alla fine, è una questione di abitudini più che di intenti.'''},
         ],
         "items": [
            {"type": "mc", "prompt": "A.1-1. L'alimentazione consapevole è：", "options": ["A) una dieta restrittiva", "B) un cambio di relazione col cibo", "C) solo una moda", "D) un errore"], "answer": 1},
            {"type": "mc", "prompt": "A.1-2. Chi pratica la mindful eating：", "options": ["A) aumenta le abbuffate", "B) riduce gli episodi di abbuffata", "C) ingrassa", "D) non cambia"], "answer": 1},
            {"type": "mc", "prompt": "A.1-3. Secondo il testo, la consapevolezza da sola：", "options": ["A) basta sempre", "B) non basta se il contesto non aiuta", "C) è inutile", "D) è perfetta"], "answer": 1},
            {"type": "mc", "prompt": "A.1-4. Tra i fattori che condizionano le scelte c'è：", "options": ["A) solo la volontà", "B) pubblicità, prezzi, tempo libero", "C) il meteo", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "A.1-5. La conclusione è che serve：", "options": ["A) una politica alimentare", "B) niente", "C) solo volontà", "D) la tecnologia"], "answer": 0},
            {"type": "mc", "prompt": "A.1-6. Il sonno è definito come：", "options": ["A) un lusso", "B) una funzione biologica essenziale", "C) una perdita di tempo", "D) un errore"], "answer": 1},
            {"type": "mc", "prompt": "A.1-7. La privazione cronica di sonno aumenta il rischio di：", "options": ["A) solo noia", "B) obesità, diabete, disturbi dell'umore", "C) nulla", "D) fame"], "answer": 1},
            {"type": "mc", "prompt": "A.1-8. Alcune aziende hanno introdotto：", "options": ["A) multe", "B) pause di sonno / orari flessibili", "C) più notti in ufficio", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "A.1-9. Recuperare il sonno richiede：", "options": ["A) tecnologia costosa", "B) disciplina e confini tra lavoro e riposo", "C) medicine", "D) nulla"], "answer": 1},
            {"type": "match", "prompt": "A.2-1. \"Fai la spesa con una lista.\" →", "options": ["A", "B"], "answer": 0},
            {"type": "match", "prompt": "A.2-2. \"Spegni gli schermi prima di dormire.\" →", "options": ["A", "B"], "answer": 1},
            {"type": "match", "prompt": "A.2-3. \"Mangia a tavola senza telefono.\" →", "options": ["A", "B"], "answer": 0},
            {"type": "match", "prompt": "A.2-4. \"Vai a letto sempre alla stessa ora.\" →", "options": ["A", "B"], "answer": 1},
            {"type": "match", "prompt": "A.2-5. \"Scegli alimenti freschi di stagione.\" →", "options": ["A", "B"], "answer": 0},
            {"type": "match", "prompt": "A.2-6. \"Evita caffè dopo le 16.\" →", "options": ["A", "B"], "answer": 1},
            {"type": "match", "prompt": "A.2-7. \"Ascolta i segnali di sazietà.\" →", "options": ["A", "B"], "answer": 0},
            {"type": "match", "prompt": "A.2-8. \"Mantieni la camera buia e fresca.\" →", "options": ["A", "B"], "answer": 1},
            {"type": "match", "prompt": "A.2-9. \"Prepara i pasti a casa.\" →", "options": ["A", "B"], "answer": 0},
            {"type": "match", "prompt": "A.2-10. \"Non usare il letto per lavorare.\" →", "options": ["A", "B"], "answer": 1},
            {"type": "open", "prompt": "A.3-1. Cosa ha fatto l'autore per migliorare il sonno?", "ref": "Ha cenato due ore prima di dormire e smesso di mangiare davanti allo schermo.", "rows": 2},
            {"type": "open", "prompt": "A.3-2. Perché dice che non è stata una \"dieta\"?", "ref": "Perché è stato un ritorno alla regolarità, non una restrizione.", "rows": 2},
            {"type": "open", "prompt": "A.3-3. Quali due \"facce della stessa medaglia\" cita?", "ref": "Alimentazione consapevole e qualità del sonno.", "rows": 2},
            {"type": "open", "prompt": "A.3-4. Secondo il testo, la salute dipende da che cosa?", "ref": "Da abitudini, più che da intenti.", "rows": 2},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 20%）",
         "tasks": [
            {"title": "B.1 — Testo personale（二选一，120–180 词）",
             "prompt": "a) Racconta un'esperienza personale in cui un'alimentazione più consapevole ha cambiato il tuo rapporto con il cibo. b) Descrivi come hai migliorato la qualità del tuo sonno e che effetti ha avuto sulla tua vita.",
             "limit": "120–180 词",
             "reference":
'''Tre anni fa il mio rapporto col cibo era caotico: saltavo i pasti, mangiavo di fronte al computer e finivo la sera pieno di sensi di colpa. Poi ho scoperto l'alimentazione consapevole. Ho iniziato a fare la spesa con una lista e a sedermi a tavola senza telefono. All'inizio è stato difficile, perché la fretta era diventata un'abitudine; però, dopo poche settimane, ho notato che assaporavo davvero ciò che mangiavo e smettevo di esagerare. Oggi non seguo diete rigide, ma ascolto la fame vera e scelgo cibi freschi. Questa lentezza mi ha ridato il piacere del cibo e, soprattutto, la calma mentale. Non è stato un cambiamento drastico, ma quotidiano: proprio come dicevo, la salute è fatta di piccole abitudini.'''},
            {"title": "B.2 — Lettera / e-mail（三选一，80–100 词）",
             "prompt": "a) Scrivi a un amico per consigliargli di migliorare il sonno. b) Scrivi all'ufficio di una palestra per chiedere informazioni su un corso di alimentazione consapevole. c) Scrivi a un collega per proporre di rendere più sana la pausa pranzo in ufficio.",
             "limit": "80–100 词",
             "reference":
'''Caro Luca, so che ultimamente dormi poco e sei sempre stanco. Ti scrivo per darti un consiglio semplice: spegni il telefono un'ora prima di dormire e vai a letto alla stessa ora. Anche evitare il caffè dopo le 16 aiuta molto. Io ho provato e, in due settimane, mi sveglio più riposato e studio meglio. Prova per qualche sera e dimmi se noti la differenza! Un abbraccio, Marco.'''},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力，权重 10%）",
         "cloze": {"cloze_text":
'''L'alimentazione consapevole _____ (1) parte dal riconoscere i propri bisogni reali. Chi mangia _____ (2) corsa spesso non distingue la fame _____ (3) la noia. Mangiare _____ (4) calma aiuta la digestione e il piacere _____ (5) cibo. Non _____ (6) una dieta rigida, ma serve l'attenzione quotidiana. Quando facciamo la spesa _____ (7) una lista, evitiamo gli acquisti impulsivi e risparmiamo _____ (8) tempo. È utile sedersi a tavola _____ (9) telefono e masticare lentamente, _____ (10) il corpo riconosce la sazietà. Chi presta attenzione _____ (11) ciò che mangia _____ (12) scopre sapori nascosti _____ (13) credeva di aver perso.

Il sonno _____ (14) una fase di riparazione per il corpo. Chi dorme poco _____ (15) più facilmente stressato e fatica _____ (16) concentrarsi. Spegnere gli schermi _____ (17) sera è una scelta utile, _____ (18) la luce blu ritarda il riposo. Anche _____ (19) pasti leggeri favoriscono il sonno, _____ (20) la qualità della vita migliora. Se andiamo a letto _____ (21) stessa ora, il corpo trova _____ (22) proprio ritmo. _____ (23) si dorme bene, ci si sveglia con più energia.''',
            "answers": ["parte","di","dalla","con","del","basta","con","del","senza","perché","a","poi","che","è","è","a","la","perché","i","e","alla","il","Se"]},
         "rewrite": [
            {"prompt": "1. Mangi lentamente. Assapori il cibo. Eviti di esagerare. → con participio presente", "ref": "Mangiando lentamente, assapori il cibo ed eviti di esagerare."},
            {"prompt": "2. Il sonno è prezioso. Lo sacrifichiamo per il lavoro. La salute ne soffre. → con «poiché»", "ref": "Poiché sacrifichiamo il sonno prezioso per il lavoro, la salute ne soffre."},
            {"prompt": "3. Fai la spesa con la lista. Eviti gli acquisti impulsivi. Risparmi. → con participio presente", "ref": "Facendo la spesa con la lista, eviti gli acquisti impulsivi e risparmi."},
            {"prompt": "4. Lo schermo ti tiene sveglia. Spegnilo prima. Dormi meglio. → con participio presente", "ref": "Spegnendo lo schermo che ti tiene sveglia, dormi meglio."},
            {"prompt": "5. L'attività fisica regolare aiuta. Riduce l'ansia. Migliora l'umore. → con «perché»", "ref": "L'attività fisica regolare aiuta perché riduce l'ansia e migliora l'umore."},
            {"prompt": "6. La dieta rigida fallisce. È troppo restrittiva. Chi la segue si demotiva. → con «perché»", "ref": "La dieta rigida fallisce perché è troppo restrittiva e chi la segue si demotiva."},
            {"prompt": "7. Mangi cibi freschi. Stai meglio. Il corpo ti ringrazia. → con participio presente", "ref": "Mangiando cibi freschi, stai meglio e il corpo ti ringrazia."},
         ],
         "wordform": [
            {"text": "1. Se _____ (mangiare) con calma, digerisci meglio.", "answers": ["mangi"]},
            {"text": "2. È importante che chi soffre di insonnia _____ (evitare) la caffeina.", "answers": ["eviti"]},
            {"text": "3. Mangiando senza fretta, si _____ (ridurre) il rischio di abbuffate.", "answers": ["riduce"]},
            {"text": "4. Il sonno _____ (considerare) essenziale per la memoria.", "answers": ["è considerato"]},
            {"text": "5. Più ci si _____ (alimentare) in modo consapevole, più si _____ (stare) bene.", "answers": ["si alimenta","sta"]},
            {"text": "6. Spero che tu _____ (riuscire) a dormire sette ore.", "answers": ["riesca"]},
            {"text": "7. Senza regolarità, la qualità del riposo _____ (peggiorare, condizionale).", "answers": ["peggiorerebbe"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力，权重 20%）",
         "items": [
            {"type": "mc", "prompt": "D.1-1. L'alimentazione consapevole significa：", "options": ["A) contare calorie", "B) ascoltare il corpo", "C) digiunare", "D) dormire"], "answer": 1},
            {"type": "mc", "prompt": "D.1-2. Il problema oggi è：", "options": ["A) il cibo", "B) la velocità", "C) il prezzo", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "D.1-3. Chi inizia vede risultati in：", "options": ["A) un giorno", "B) tre settimane", "C) un anno", "D) mai"], "answer": 1},
            {"type": "mc", "prompt": "D.1-4. Tra i risultati c'è：", "options": ["A) più energia", "B) più fame", "C) sonno peggiore", "D) nulla"], "answer": 0},
            {"type": "mc", "prompt": "D.1-5. L'azienda è a：", "options": ["A) Roma", "B) Torino", "C) Milano", "D) Napoli"], "answer": 1},
            {"type": "mc", "prompt": "D.1-6. La stanza del sonno permette di riposare：", "options": ["A) 5 minuti", "B) 20 minuti", "C) 2 ore", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "D.1-7. Il riposo è：", "options": ["A) prima di pranzo", "B) dopo pranzo", "C) la sera", "D) mattina"], "answer": 1},
            {"type": "mc", "prompt": "D.1-8. Gli errori sono calati del：", "options": ["A) 5%", "B) 15%", "C) 50%", "D) 100%"], "answer": 1},
            {"type": "mc", "prompt": "D.1-9. Il fondatore dice：", "options": ["A) chi dorme decide meglio", "B) chi corre vince", "C) nulla", "D) chi mangia vince"], "answer": 0},
            {"type": "mc", "prompt": "D.1-10. Aziende che copiano il modello：", "options": ["A) 10", "B) 100", "C) 1000", "D) 1"], "answer": 1},
            {"type": "cloze", "text": "D.2-1. Due anni fa dormiva ________ ore.", "answers": ["quattro"]},
            {"type": "cloze", "text": "D.2-2. Mangiava ________ (in modo disordinato).", "answers": ["in modo disordinato"]},
            {"type": "cloze", "text": "D.2-3. Ora mangia ________ e senza telefono.", "answers": ["seduta"]},
            {"type": "cloze", "text": "D.2-4. Va a letto alle ________.", "answers": ["23"]},
            {"type": "cloze", "text": "D.2-5. Fa yoga ________ volte a settimana.", "answers": ["tre"]},
            {"type": "cloze", "text": "D.2-6. Si sveglia alle ________.", "answers": ["7"]},
            {"type": "cloze", "text": "D.2-7. Si sente ________.", "answers": ["in forma"]},
            {"type": "cloze", "text": "D.2-8. Dice che non è ________.", "answers": ["perfetto"]},
            {"type": "cloze", "text": "D.2-9. Il suo consiglio: iniziare ________.", "answers": ["piano"]},
            {"type": "cloze", "text": "D.2-10. Il tema del testo è ________ e sonno / stile di vita.", "answers": ["alimentazione / stile di vita"]},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语，权重 30%）",
         "tasks": [
            {"desc":
'''① 描述图片并回答；② 概述短文并回答；③ 角色扮演。
任务：① 描述图片：一个人平静地做饭，不用手机，与家人坐在桌前；并回答"Secondo te, mangiare piano è davvero importante per la salute?"；② 概述 Testo A3（2–3 句）并回答"Il sonno è una questione solo privata o anche sociale?"；③ 角色扮演：你是营养师，考官说"Non ho tempo di mangiare bene"，你用实用论据反驳（lista della spesa, pasti a casa）。''',
             "points": 50,
             "rubric":
'''① 图片描述具体（calma, famiglia, senza telefono），并用论证支撑观点；② 摘要准确抓住 Testo A3 核心（regolarità, due facce della stessa medaglia），并能上升到"sonno come questione sociale"；③ 角色扮演以 nutrizionista 身份给可行建议，应对"non ho tempo"；④ 语法（虚拟 / 条件 / 关系代词）较准确；⑤ 流利度与互动。''',
             "dims": [
                ("Pronuncia 发音", "发音标准，语域与场合匹配"),
                ("Fluenza 流利度", "表达连贯，能展开论述与评论"),
                ("Grammatica 语法", "虚拟 / 条件 / 关系代词较准确"),
                ("Contenuto 内容", "概述完整、立场清晰，论证有逻辑"),
                ("Interazione 互动", "听证会角色扮演说服力强"),
             ],
             "ref":
'''Nella figura vedo una persona che cucina con calma, senza telefono, seduta a tavola con la famiglia: un'immagine di alimentazione consapevole. Secondo me mangiare piano è davvero importante per la salute, perché rallentare aiuta la digestione e il piacere del cibo. Il Testo A3 dice che alimentazione consapevole e qualità del sonno sono due facce della stessa medaglia: entrambe richiedono attenzione e regolarità. Il sonno non è solo privato, ma anche sociale, perché dipende da orari di lavoro e servizi pubblici. Signor cliente, non ha tempo di mangiare bene? Le consiglio due gesti semplici: fare la spesa con una lista per evitare acquisti impulsivi, e preparare i pasti a casa. Così risparmia tempo e sta meglio!'''},
         ]},
    ],
})

# ============================== C1 =========================================
LEVELS.append({
    "code": "C1", "name": "CELI 4",
    "subtitle": "sanità pubblica / invecchiamento della popolazione",
    "theme": "🥗 Salute, alimentazione e benessere", "subj_max": 50,
    "audio": [
        {"title": "Intervista — Demografa（sanità e invecchiamento）", "body":
'''L'invecchiamento non è un'emergenza medica, è una questione di welfare. Oggi in Italia oltre il 23% della popolazione ha più di 65 anni. Servono tre cose: sanità territoriale vicina, case a misura di anziano, e ponti tra generazioni. Altrimenti rischiamo solitudine e costi ospedalieri alti. La mia proposta: un'ora su cinque di volontariato intergenerazionale a scuola. Non è utopia, è civiltà.'''},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，权重 20%）",
         "texts": [
            {"title": "Testo 1 — Articolo accademico（sanità pubblica）", "body":
'''Le statistiche dell'OCSE indicano che i sistemi sanitari pubblici universali garantiscono aspettative di vita più alte a costi pro capite inferiori rispetto ai modelli fondati sulle assicurazioni private. Tuttavia, la sostenibilità di questi sistemi dipende dalla capacità di prevenire anziché curare. La spesa per la cronicità assorbe oggi oltre il 70% dei bilanci sanitari nei paesi avanzati. Senza una riforma che sposti risorse dalla cura ospedaliera alla sanità territoriale, il diritto alle cure rischia di restare sulla carta per le fasce più deboli.'''},
            {"title": "Testo 2 — Intervento opinionista（invecchiamento della popolazione）", "body":
'''Mentré i demografi parlano di "inverno demografico", resta sottotaciuto un fatto: invecchiare non è solo un costo, è anche una risorsa. Gli anziani curano nipoti, mantengono reti di vicinato, trasmettono mestieri. Ridurre la questione a un buco nei conti pubblici è miope. Certo, servono pensioni eque e sanità accessibile; ma il panico sulla natalità nasconde spesso la riluttanza a investire davvero nei giovani. Una società che non pensa ai nonni non penserà nemmeno ai nipoti.'''},
         ],
         "items": [
            {"type": "mc", "prompt": "1. I sistemi pubblici universali：", "options": ["A) costano di più pro capite", "B) danno vita più lunga a minor costo", "C) funzionano peggio", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "2. La sostenibilità dipende da：", "options": ["A) curare di più", "B) prevenire anziché curare", "C) niente", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "3. La cronicità assorbe oltre：", "options": ["A) il 50% dei bilanci", "B) il 70% dei bilanci", "C) il 30%", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "4. Il tono del Testo 2 è：", "options": ["A) neutrale", "B) critico / polemico", "C) pubblicitario", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "5. Per il Testo 2, gli anziani sono：", "options": ["A) solo un costo", "B) anche una risorsa", "C) inutili", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "6. Entrambi i testi concordano sul fatto che：", "options": ["A) il sistema è perfetto", "B) servono risorse e riforme", "C) il lavoro finirà", "D) nulla"], "answer": 1},
            {"type": "tf", "prompt": "7. I modelli privati costano meno pro capite dei pubblici. (V/F)", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "8. La spesa per la cronicità è un tema centrale del Testo 1. (V/F)", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "9. Il Testo 2 sostiene che invecchiare è solo un costo. (V/F)", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "10. Gli anziani trasmettono mestieri, secondo il Testo 2. (V/F)", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "11. I due testi hanno posizioni identiche su tutto. (V/F)", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "12. Per l'opinionista, il panico sulla natalità nasconde riluttanza a investire nei giovani. (V/F)", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 30%）",
         "tasks": [
            {"title": "Compito a — Riassunto（摘要，约 80–100 词）",
             "prompt": "Sintetizza le due posizioni dei testi in italiano corretto: Testo 1 (sanità pubblica) e Testo 2 (invecchiamento come risorsa).",
             "limit": "80–100 词",
             "reference":
'''Il Testo 1, di tono accademico, sostiene che i sistemi sanitari pubblici universali garantiscono vita più lunga a minor costo, ma la loro sostenibilità esige prevenzione e sanità territoriale, perché la cronicità divora oltre il 70% dei bilanci. Il Testo 2, polemico, ribalta il luogo comune: invecchiare non è solo un costo, è anche risorsa (nonni, vicinato, mestieri). Entrambi convengono che occorrono riforme e risorse, e che ridurre tutto a numeri nei conti pubblici è miope. Resta il nodo: come finanziare equità e sostenibilità insieme.'''},
            {"title": "Compito b — Saggio / articolo（议论文，约 150–180 词）",
             "prompt": "\"Il diritto alle cure e l'invecchiamento della popolazione: come conciliare equità e sostenibilità?\" Sviluppa la tua tesi con argomenti e un esempio.",
             "limit": "150–180 词（totale 200–250）",
             "reference":
'''Il diritto alle cure e l'invecchiamento della popolazione possono convivere solo se la sanità smette di essere solo ospedaliera e diventa territoriale. Come osserva il Testo 1, la cronicità assorbe oltre il 70% dei bilanci: se non spostiamo risorse dalla cura alla prevenzione, il diritto alle cure resterà sulla carta per i più deboli. Al tempo stesso, il Testo 2 ci ricorda che gli anziani sono una risorsa, non un puro onere. A mio avviso, equità e sostenibilità si conciliano con un patto generazionale: case a misura di anziano e ponti tra generazioni riducono solitudine e costi. Un esempio concreto: un'ora su cinque di volontariato intergenerazionale a scuola trasforma gli anziani da "peso" a mentori. In conclusione, investire nella prevenzione e nel legame tra generazioni non è carità, è la condizione stessa di una sanità pubblica davvero universale.'''},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力，权重 10%）",
         "cloze": {"cloze_text":
'''La sanità pubblica _____ (1) risorse stabili per funzionare. Chi non _____ (2) non spende di più solo dopo, ma _____ (3) il sistema nel lungo periodo. È _____ (4) una rete territoriale capillare, perché le cure _____ (5) garantite a tutti i cittadini. Un modello _____ (6) riduce le disuguaglianze sociali e migliora la _____ (7) media della popolazione. Tuttavia, _____ (8) gli ospedali siano utili, essi non _____ (9) a risolvere tutto: serve _____ (10) patto tra le generazioni. Se lo Stato non _____ (11), il divario _____ (12) e a pagarne il prezzo _____ (13) i più deboli.

L'invecchiamento della popolazione _____ (14) una questione di welfare, non solo medica. Oggi in Italia oltre il 23% delle persone _____ (15) più di 65 anni. _____ (16) necessario ripensare i servizi, _____ (17) le case siano a misura di anziano. È importante che i nonni _____ (18) il loro ruolo sociale, e che i giovani _____ (19) a conoscerli meglio. _____ (20) si investisse nella solidarietà tra generazioni, il costo _____ (21) sarebbe minore. Un'ora su cinque di volontariato _____ (22) una risorsa, non _____ (23) perdita di tempo.''',
            "answers": ["richiede","previene","compromette","necessaria","vanno","adeguato","salute","Benché","bastano","un","interviene","si allarga","sono","è","hanno","È","affinché","mantengano","imparino","Se","sociale","è","una"]},
         "rewrite": [
            {"prompt": "1. (passivo) Lo Stato tutela la salute di tutti. →", "ref": "La salute di tutti è tutelata dallo Stato."},
            {"prompt": "2. (relativo) Il welfare è un diritto. Il welfare protegge gli anziani. →", "ref": "Il welfare è un diritto che protegge gli anziani."},
            {"prompt": "3. (congiuntivo) È giusto. Tutti possono curarsi. →", "ref": "È giusto che tutti possano curarsi."},
            {"prompt": "4. (se + condizionale) Lo Stato non interviene. Le disuguaglianze aumentano. →", "ref": "Se lo Stato non intervenisse, le disuguaglianze aumenterebbero."},
            {"prompt": "5. (participio) Investiamo nei giovani. Così riduciamo i costi futuri. →", "ref": "Investendo nei giovani, riduciamo i costi futuri."},
            {"prompt": "6. (malgrado + congiuntivo) I costi sono alti. Dobbiamo investire nella prevenzione. →", "ref": "Malgrado i costi siano alti, dobbiamo investire nella prevenzione."},
            {"prompt": "7. (consecutiva) La popolazione invecchia. Il sistema sanitario è sotto pressione. →", "ref": "La popolazione invecchia al punto che il sistema sanitario è sotto pressione."},
         ],
         "wordform": [
            {"text": "1. Sarebbe giusto che tutti _____ (potere) curarsi.", "answers": ["potessero"]},
            {"text": "2. Senza prevenzione, la spesa sanitaria _____ (aumentare, condizionale).", "answers": ["aumenterebbe"]},
            {"text": "3. Le cure _____ (garantire, passivo) dalla Costituzione.", "answers": ["sono garantite"]},
            {"text": "4. È lo Stato _____ (che / cui / a cui) tutela la salute.", "answers": ["che"]},
            {"text": "5. _____ (Malgrado / Malgrado che) i costi, investiamo nei giovani.", "answers": ["Malgrado"]},
            {"text": "6. Preferisco che tu _____ (venire) a trovare i nonni.", "answers": ["venga"]},
            {"text": "7. Se il governo _____ (investire) di più, gli anziani _____ (stare, condizionale) meglio.", "answers": ["investisse","starebbero"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力，权重 15%）",
         "items": [
            {"type": "cloze", "text": "Tabella 1. % popolazione italiana con più di 65 anni: ________.", "answers": ["23%"]},
            {"type": "cloze", "text": "Tabella 2. Seconda cosa necessaria: ________.", "answers": ["case a misura di anziano"]},
            {"type": "cloze", "text": "Tabella 3. Ore su 5 da dedicare al volontariato: ________.", "answers": ["un'ora su cinque (1 su 5)"]},
            {"type": "tf", "prompt": "V/F 4. La demografa dice che l'invecchiamento è solo un'emergenza medica.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "V/F 5. I ponti tra generazioni servono, per la demografa.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "V/F 6. La proposta di 1 ora su 5 è definita \"utopia\".", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "V/F 7. Il rischio è solitudine e costi ospedalieri alti.", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语，权重 25%）",
         "tasks": [
            {"desc":
'''带材料面试（长篇论述 + 深度讨论）。
Materiale：Breve testo su invecchiamento e risorsa (Testo 2).
Task：① 用 2–3 分钟阐述立场："La società deve investire negli anziani come risorsa, non solo come costo. Sei d'accordo?"；② 讨论：回应考官反驳（es. "Ma le pensioni pesano sui giovani"）并提出具体措施（volontariato intergenerazionale）。''',
             "points": 50,
             "rubric":
'''① 长篇论述结构清晰（tesi → argomenti → esempio），语域 formal / argomentativo；② 熟练使用 congiuntivo, condizionale, passivo, relativo；③ 讨论中能承接考官反驳并给出具体措施；④ 词汇精准（sostenibilità, equità, cronicità, welfare）；⑤ 发音流利、衔接自然。''',
             "dims": [
                ("Pronuncia 发音", "发音精准，语调节奏自如"),
                ("Fluenza 流利度", "长篇论述流畅，衔接自然"),
                ("Grammatica 语法", "虚拟 / 条件 / 被动准确，句式丰富"),
                ("Contenuto 内容", "立场明确，词汇丰富（sostenibilità, equità, cronicità, welfare）"),
                ("Interazione 互动", "深度讨论中回应质疑，逻辑自洽"),
             ],
             "ref":
'''La mia posizione è che la società deve investire negli anziani come risorsa, non solo come costo. Il Testo 2 ha ragione: gli anziani curano nipoti, mantengono reti di vicinato e trasmettono mestieri; ridurre tutto a un buco nei conti pubblici è miope. Certo, le pensioni pesano sui giovani, ma la risposta non è tagliare, bensì costruire ponti tra generazioni. La mia proposta concreta è un'ora su cinque di volontariato intergenerazionale a scuola: così gli anziani diventano mentori e i giovani risparmiano costi sociali futuri. Occorrono però anche risorse: una sanità territoriale vicina e case a misura di anziano riducono solitudine e spesa ospedaliera. In conclusione, equità e sostenibilità si conciliano solo con un patto generazionale che valorizzi la persona anziana come risorsa, non come puro onere.'''},
         ]},
    ],
})

# ============================== C2 =========================================
LEVELS.append({
    "code": "C2", "name": "CELI 5",
    "subtitle": "bioetica e salute / medicalizzazione della società",
    "theme": "🥗 Salute, alimentazione e benessere", "subj_max": 50,
    "audio": [
        {"title": "Dibattito — Bioeticista e sociologo", "body":
'''Bioeticista: La medicalizzazione ci spoglia dell'agency; la bioetica deve ridare alla persona la titolarità del proprio vissuto.
Sociologo: Attenzione: non ogni diagnosi è oppressione. Ma ha ragione sul rischio di mercificare l'emozione.
Bioeticista: Non è negare la scienza, è difendere il confine. Se tutto è sintomo, nulla è scelta.
Sociologo: Allora distinguiamo cura da gestione. Punto di sintesi: bioetica come critica, non come notaio del mercato.'''},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读，权重 20%）",
         "texts": [
            {"title": "Testo — Saggio（bioetica e medicalizzazione della società）", "body":
'''Esiste una forma silenziosa di colonizzazione: quella che trasforma ogni esperienza umana in sintomo. La medicalizzazione della società non è un complotto, è una deriva dolce. Il lutto diventa "disturbo dell'adattamento", la timidezza "fobia sociale", la stanchezza "astenia". Così facendo, sottraiamo alla persona la responsabilità del proprio vissuto e la consegniamo alla prescrizione. La bioetica, nata per proteggere la vita dalle tecnologie, rischia oggi di ridursi a un comitato di notabili che autorizza ciò che il mercato già decide. La posta in gioco non è clinica: è l'idea stessa di soggettività. Una società che patologizza tutto finisce per non curare più nessuno, ma solo gestire casi.'''},
         ],
         "items": [
            {"type": "mc", "prompt": "1. (metafora) «Colonizzazione silenziosa» metaforizza：", "options": ["A) la guerra", "B) trasformare esperienze in sintomi", "C) la scuola", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "2. (posizione) La medicalizzazione è vista come：", "options": ["A) un complotto", "B) una deriva dolce / processo morbido", "C) un progresso puro", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "3. (dettaglio) Il lutto diventa：", "options": ["A) normalità", "B) \"disturbo dell'adattamento\"", "C) una festa", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "4. (inferenza) Sottraendo la responsabilità, la persona è consegnata a：", "options": ["A) se stessa", "B) la prescrizione", "C) la famiglia", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "5. (inferenza) La bioetica rischia di ridursi a：", "options": ["A) difesa della vita", "B) comitato di notabili che autorizza il mercato", "C) nulla", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "6. (interpretazione) «La posta in gioco non è clinica» significa che il nucleo è：", "options": ["A) un problema medico", "B) l'idea di soggettività / identità", "C) nulla", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "7. (tono) Il tono del testo è：", "options": ["A) neutrale", "B) critico / ironico", "C) pubblicitario", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "8. (conclusione) Patologizzare tutto porta a：", "options": ["A) curare tutti", "B) non curare più nessuno, solo gestire casi", "C) guarire", "D) nulla"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作，权重 30%）",
         "tasks": [
            {"title": "Compito 1 — Saggio / articolo（约 200–250 词）",
             "prompt": "\"La società medicalizza troppo la vita quotidiana? Fino a che punto la bioetica può opporsi al mercato della salute?\" Sviluppa una tesi articolata, con riferimenti a soggettività, mercato e responsabilità.",
             "limit": "200–250 词",
             "reference":
'''La società medicalizza troppo la vita quotidiana? La risposta non è clinica, è politica. Quando il lutto diventa "disturbo dell'adattamento" e la timidezza "fobia sociale", non curiamo: spostiamo la responsabilità del vissuto dalla persona alla prescrizione. È una deriva dolce, non un complotto, ma produce effetti reali sull'autonomia. La bioetica nacque per proteggere la vita dalle tecnologie; oggi rischia invece di fare da notaio al mercato della salute, autorizzando ciò che il mercato già decide. Fino a che punto può opporsi? Solo se recupera la sua vocazione critica: ridare alla persona la titolarità del proprio dolore, distinguendo cura da gestione. Non nego la scienza — una diagnosi può salvare chi soffre davvero —, ma respingo una società che patologizza tutto e finisce per non curare più nessuno, ma solo gestire casi. La posta in gioco è la soggettività stessa: una comunità che confonde ogni emozione con un sintomo consegna al mercato ciò che appartiene alla libertà. La bioetica, dunque, non deve abolire la medicina, ma difendere il confine tra cura e controllo.'''},
            {"title": "Compito 2 — Seconda prova（评论 / intervento，约 60–80 词）",
             "prompt": "Scrivi un intervento per un festival di filosofia in cui difendi il diritto a non essere \"pazienti\" per ogni emozione umana（tono saggistico / civico）.",
             "limit": "60–80 词",
             "reference":
'''Cittadini e pensatori, difendiamo il diritto a non essere "pazienti" per ogni emozione umana. La tristezza non è sempre una malattia, e il lutto non è un errore da correggere. Quando tutto diventa sintomo, nulla è più scelta. Rivendichiamo la soggettività: il dolore va ascoltato, non solo prescritto. La medicina curi, la mercificazione no. La libertà comincia dove finisce la medicalizzazione dell'esistenza.'''},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力，权重 10%）",
         "cloze": {"cloze_text":
'''La medicalizzazione _____ (1) lo spazio dell'esperienza comune e _____ (2) la persona della sua titolarità. Chi _____ (3) la tristezza la sottrae al senso _____ (4) umano, trasformando _____ (5) emozione in sintomo. È _____ (6) che la bioetica resista prima che il mercato _____ (7) il vissuto. Non si tratta di _____ (8) rifiuto della scienza, bensì di _____ (9) alla persona la sua soggettività. La società _____ (10) uscirà migliore, _____ (11) mantenga il confine tra cura e controllo. _____ (12) tutto è sintomo, nulla _____ (13) scelta.

La bioetica nacque _____ (14) proteggere la vita dalle tecnologie, ma oggi rischia _____ (15) a notaio del mercato della salute. _____ (16) si difenda il confine tra cura e gestione, la libertà non _____ (17) illusoria. Occorre _____ (18) un quadro critico _____ (19) la mercificazione dell'emozione. Non _____ (20) la scienza — una diagnosi può salvare _____ (21) soffre davvero —, ma respingo _____ (22) società che patologizza _____ (23).''',
            "answers": ["erode","spoglia","patologizza","più","un'","auspicabile","fagociti","un","ridare","ne","purché","Se","è","per","di ridursi","Solo se","diventa","elaborare","contro","nego","chi","una","tutto"]},
         "rewrite": [
            {"prompt": "1. (passivo) La società medicalizza ogni emozione. →", "ref": "Ogni emozione è medicalizzata dalla società."},
            {"prompt": "2. (participio assoluto) La posta in gioco era chiara. Abbiamo agito di conseguenza. →", "ref": "Posta la posta in gioco, abbiamo agito di conseguenza."},
            {"prompt": "3. (concessiva + congiuntivo) Il mercato fagocita il vissuto. Noi resistiamo. →", "ref": "Benché il mercato fagociti il vissuto, noi resistiamo."},
            {"prompt": "4. (relativa complessa) La soggettività va rispettata. La soggettività è ciò che ci rende liberi. →", "ref": "La soggettività, che è ciò che ci rende liberi, va rispettata."},
            {"prompt": "5. (non tanto…quanto) Non conta la cura. Conta il confine. →", "ref": "Non tanto la cura, quanto il confine conta."},
            {"prompt": "6. (invece di) Non curiamo. Spostiamo la responsabilità sulla prescrizione. →", "ref": "Invece di curare, spostiamo la responsabilità sulla prescrizione."},
            {"prompt": "7. (consecutiva) La diagnosi è precoce. Può salvare chi soffre. →", "ref": "La diagnosi è così precoce da poter salvare chi soffre."},
         ],
         "wordform": [
            {"text": "1. La medicalizzazione _____ (erodere) lo spazio dell'esperienza comune.", "answers": ["erode"]},
            {"text": "2. È _____ (auspicabile / auspicabilmente) che la bioetica resista.", "answers": ["auspicabile"]},
            {"text": "3. Chi _____ (patologizzare) la tristezza la sottrae al senso umano.", "answers": ["patologizza"]},
            {"text": "4. Non si tratta di un rifiuto, bensì di _____ (ridare) la soggettività.", "answers": ["ridare"]},
            {"text": "5. La società _____ (uscire, condizionale) migliore, purché mantenga il confine.", "answers": ["uscirebbe"]},
            {"text": "6. È il limite _____ (in cui / dove / che) si protegge la persona.", "answers": ["in cui"]},
            {"text": "7. _____ (Né / Ne / Non) la clinica né il mercato decidono tutto.", "answers": ["Né"]},
            {"text": "8. Che _____ (si riconoscere) la soggettività è essenziale.", "answers": ["si riconosca"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力，权重 15%）",
         "items": [
            {"type": "mc", "prompt": "1. (atteggiamento) Il bioeticista vede la medicalizzazione come：", "options": ["A) progresso", "B) perdita di agency / sottrazione di titolarità", "C) errore", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "2. (atteggiamento) Il sociologo teme che：", "options": ["A) aiuti troppo", "B) si mercifichi l'emozione", "C) costi poco", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "3. (sintesi) Il punto di sintesi è：", "options": ["A) bioetica come notaio del mercato", "B) bioetica come critica", "C) abolire la bioetica", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "4. (relazione) Atteggiamento dello sociologo verso il bioeticista：", "options": ["A) totale disaccordo", "B) parziale convergenza", "C) indifferenza", "D) nulla"], "answer": 1},
            {"type": "mc", "prompt": "5. (significato) «Se tutto è sintomo, nulla è scelta» esprime：", "options": ["A) favore alla medicalizzazione", "B) critica alla perdita di autonomia", "C) nulla", "D) nulla"], "answer": 1},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语，权重 25%）",
         "tasks": [
            {"desc":
'''抽象话题（哲学 / 社会伦理）演讲 + 批判性质疑回应。
Task：① 准备 3–4 分钟演讲："Fino a che punto la società ha il diritto di trasformare la sofferenza in malattia?" 语域 saggistico；② 考官提出质疑（es. "Ma la diagnosi aiuta chi soffre davvero"），你以 rigorosa argomentazione 反驳。''',
             "points": 50,
             "rubric":
'''① 演讲具 saggistica / 哲思语域，善用 metafora, ironia, contrapposizione（cura vs gestione, soggettività vs mercato）；② 句法复杂且准确（虚拟 / 条件 / 被动 / incisi）；③ 能承接考官质疑并以 rigorosa argomentazione 反驳；④ 词汇高级（agency, soggettività, titolarità, medicalizzazione, patologizzare）；⑤ 发音地道、节奏自如。''',
             "dims": [
                ("Pronuncia 发音", "发音精准，学术语域自如"),
                ("Fluenza 流利度", "演讲连贯，抽象概念流转自然"),
                ("Grammatica 语法", "复杂句法准确（虚拟 / 条件 / 被动 / 关系）"),
                ("Contenuto 内容", "抽象概念清晰，词汇精准（agency, soggettività, titolarità, medicalizzazione）"),
                ("Pensiero critico 思辨", "批判性回应质疑，逻辑自洽有深度"),
             ],
             "ref":
'''Fino a che punto la società ha il diritto di trasformare la sofferenza in malattia? A mio avviso, quel diritto si arresta dove comincia la sottrazione di titolarità: quando il lutto diventa "disturbo dell'adattamento" e la timidezza "fobia sociale", non curiamo, ma spostiamo la responsabilità del vissuto dalla persona alla prescrizione. È una deriva dolce, non un complotto, ma erode l'autonomia. A chi obietta "la diagnosi aiuta chi soffre davvero" rispondo con la distinzione tra cura e gestione: una diagnosi può salvare, ma se tutto è sintomo, nulla è più scelta. La bioetica non deve abolire la medicina, bensì ridare alla persona la soggettività del proprio dolore, difendendo il confine tra cura e controllo. La posta in gioco non è clinica: è l'idea stessa di libertà. Una società che patologizza tutto finisce per non curare più nessuno, ma solo gestire casi. Dunque il diritto della società si ferma dove inizia l'agency del singolo.'''},
         ]},
    ],
})

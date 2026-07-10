# -*- coding: utf-8 -*-
"""Dati strutturati del Vol.2 degli esami CELI (A1-C2).
Tema: Era digitale, social e intelligenza artificiale
(数字时代、社交媒体与人工智能).
Questo modulo è consumato dal generatore: la struttura di LEVELS,
sections, items e campi è identica a quella attesa dal motore di
rendering (vedi Vol.3 di riferimento).
"""

VOL_NO = 2
THEME_EMOJI = "📱"
THEME_TEXT = "数字时代、社交媒体与人工智能"

LEVELS = []

# ============================== A1 =========================================
LEVELS.append({
    "code": "A1", "name": "CELI Impatto",
    "subtitle": "il mio telefono / messaggi e chiamate",
    "theme": "📱 数字时代、社交媒体与人工智能", "subj_max": 20,
    "audio": [],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo A — Un messaggio", "body":
"""Ciao Luca! Il mio nuovo telefono è blu. È molto bello. Ti mando un messaggio ogni giorno. Stasera chiamami alle 20. A presto! — Giulia"""},
            {"title": "Testo B — Un avviso", "body":
"""Centro Telefoni — Aperto dal lunedì alla domenica. Orario: 9:00 – 19:30. Ripariamo telefoni e vendiamo cover. Piazza Garibaldi 5, Milano."""},
            {"title": "Testo C — Un biglietto", "body":
"""Cara nonna, grazie per il telefono! Ora mando messaggi alla mamma. La chiamata è chiara. Ti voglio bene! — Tuo nipote Pietro"""},
         ],
         "items": [
            {"type": "match", "prompt": "1. Un negozio di telefoni.", "options": ["A", "B", "C"], "answer": 1},
            {"type": "match", "prompt": "2. Un messaggio a un amico.", "options": ["A", "B", "C"], "answer": 0},
            {"type": "match", "prompt": "3. Un biglietto per la nonna.", "options": ["A", "B", "C"], "answer": 2},
            {"type": "mc", "prompt": "4. Di che colore è il telefono di Giulia?", "options": ["A. rosso", "B. blu", "C. verde"], "answer": 1},
            {"type": "mc", "prompt": "5. A che ora chiude il Centro Telefoni?", "options": ["A. alle 19:30", "B. alle 20:00", "C. alle 9:00"], "answer": 0},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Scrivi un messaggio a un amico (biglietto / messaggio)",
             "prompt": "Il tuo telefono nuovo è rotto. Scrivi un breve messaggio a un tuo amico (Marco): ① il tuo telefono è nero e molto vecchio; ② stasera non puoi chiamarlo; ③ chiedigli di mandarti un messaggio domani. Inizia con \"Ciao Marco,\". 30–50 parole.",
             "limit": "30–50 词",
             "reference":
"""Ciao Marco, il mio telefono è nero e molto vecchio. Stasera non posso chiamarti perché è rotto. Mandami un messaggio domani, per favore! A domani. — Tuo amico"""},
         ]},
        {"kind": "oral", "title": "3. Prova orale（口语，含听力评定）",
         "tasks": [
            {"desc":
"""CELI A1 无独立听力卷，听力并入口语评定。考官先朗读简短指令/问题（模拟音频文本），考生听懂并回应，再进入引导问答。
① 考官引导问答（姓名 / 年龄 / 住址 / 日常 / 手机）：1. Come ti chiami? 2. Quanti anni hai? 3. Dove abiti? 4. Hai un telefono? Di che colore è? 5. Mandi messaggi ai tuoi amici?
② 简单表达：用 2–3 句话说一说你最喜欢用手机做什么（es. «Chiamo la mamma. Mando foto.»）。""",
             "points": 10,
             "rubric":
"""能听懂考官简短问题并作答（听力评定）；使用 presente / avere / 基础词汇（telefono, messaggio, chiamare）；发音可懂；完成 4–5 个问答即合格。""",
             "dims": [
                ("Pronuncia 发音", "单音基本准确，语调自然，能听懂简单指令"),
                ("Fluenza 流利度", "能用基本词汇与单句作答，自我介绍连贯"),
                ("Grammatica 语法", "使用基础句型(essere/avere/presente)，错误不影响理解"),
                ("Contenuto 内容", "覆盖姓名 / 年龄 / 住址 / 手机使用等任务要求"),
                ("Interazione 互动", "能回应考官提问，维持简短交流"),
             ],
             "ref":
"""Buongiorno, mi chiamo Giulia e ho dodici anni. Abito a Milano con i miei genitori e ho un telefono blu. Mando messaggi ai miei amici ogni giorno e la sera chiamo la mamma. Mi piace molto usare il telefono per fare foto e giocare. Il mio amico Marco ha un gatto e glielo mostro con una foto. Secondo te, a che ora chiami i tuoi amici?"""},
         ]},
    ],
})

# ============================== A2 =========================================
LEVELS.append({
    "code": "A2", "name": "CELI 1",
    "subtitle": "i social network / un video che diventa virale",
    "theme": "📱 数字时代、社交媒体与人工智能", "subj_max": 30,
    "audio": [
        {"title": "Dialogo 1 — Madre e figlia", "body":
"""— Mamma, posso usare il tablet?
— Sì, ma solo 30 minuti. Poi fai i compiti.
— Va bene, grazie!"""},
        {"title": "Dialogo 2 — Annuncio radio", "body":
"""Buongiorno! Oggi parliamo di un video virale: un cane che suona la chitarra ha 2 milioni di mi piace. Il proprietario è un ragazzo di Napoli."""},
        {"title": "Dialogo 3 — Pubblicità", "body":
"""Compra il nuovo telefono SuperX: fotocamera da 50 megapixel, solo 199 euro!"""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo A — Post su un blog", "body":
"""Ciao a tutti! Sono Chiara e ho 15 anni. Ieri ho pubblicato un video su TikTok: ballavo in cucina con il mio gatto. Oggi il video ha un milione di visualizzazioni! Non ci credo. È diventato virale in poche ore."""},
            {"title": "Testo B — Avviso di sicurezza", "body":
"""Genitori attenzione! I bambini usano i social network ogni giorno. Controllate la privacy. Non pubblicate foto dei figli senza permesso. Parlate con loro di internet."""},
            {"title": "Testo C — Pubblicità", "body":
"""SocialStar App — Nuova app gratuita! Fai video, aggiungi musica e diventi famoso. Scarica ora su Google Play e App Store."""},
         ],
         "items": [
            {"type": "match", "prompt": "1. Un consiglio per le famiglie.", "options": ["A", "B", "C"], "answer": 1},
            {"type": "match", "prompt": "2. La storia di un video virale.", "options": ["A", "B", "C"], "answer": 0},
            {"type": "match", "prompt": "3. La presentazione di un'applicazione.", "options": ["A", "B", "C"], "answer": 2},
            {"type": "mc", "prompt": "4. Dove ha pubblicato il video Chiara?", "options": ["A. su Instagram", "B. su TikTok", "C. su Facebook"], "answer": 1},
            {"type": "mc", "prompt": "5. Chi deve controllare la privacy secondo l'avviso?", "options": ["A. i bambini", "B. i genitori", "C. i professori"], "answer": 1},
            {"type": "mc", "prompt": "6. SocialStar App è…", "options": ["A. a pagamento", "B. gratuita", "C. solo per computer"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito 1 — Completamenti（补全短文）",
             "prompt": "Completa il testo con le parole: video / amici / internet / telefono. \"Il mio _____ è sempre con me. Uso _____ per parlare con i miei _____. Ieri ho visto un _____ divertente su YouTube. Mi piace la tecnologia!\"",
             "limit": "填空",
             "reference": "Il mio telefono è sempre con me. Uso internet per parlare con i miei amici. Ieri ho visto un video divertente su YouTube. Mi piace la tecnologia!"},
            {"title": "Compito 2 — Espansione（扩写留言，50–80 词）",
             "prompt": "Da questo messaggio breve scrivi un testo più lungo (50–80 parole): \"Paolo non può uscire stasera, perché studia per un esame di informatica.\" Spiega chi è Paolo, perché studia al computer, che materia gli piace, e cosa farete nel fine settimana.",
             "limit": "50–80 词",
             "reference":
"""Paolo è il mio compagno di classe. Non può uscire stasera perché studia per un esame di informatica. Usa il computer per prepararsi e gli piace molto quella materia. Nel fine settimana andremo al cinema insieme."""},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力）",
         "items": [
            {"type": "match", "prompt": "1. Una pubblicità.", "options": ["Dialogo 1", "Dialogo 2", "Dialogo 3"], "answer": 2},
            {"type": "match", "prompt": "2. Una conversazione in famiglia.", "options": ["Dialogo 1", "Dialogo 2", "Dialogo 3"], "answer": 0},
            {"type": "match", "prompt": "3. Una notizia radiofonica.", "options": ["Dialogo 1", "Dialogo 2", "Dialogo 3"], "answer": 1},
            {"type": "mc", "prompt": "4. Quante minuti può usare il tablet la figlia?", "options": ["A. 30", "B. 60", "C. 15"], "answer": 0},
            {"type": "mc", "prompt": "5. Di che cosa parla il video virale alla radio?", "options": ["A. un gatto", "B. un cane che suona", "C. un bambino"], "answer": 1},
            {"type": "mc", "prompt": "6. Quanto costa il telefono SuperX?", "options": ["A. 99 euro", "B. 199 euro", "C. 299 euro"], "answer": 1},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 自我介绍 + 习惯爱好：Parla di te e di come usi i social network（2–3 分钟）。
② 描述图片：描述一张「年轻人拍视频」的图片（cosa fanno? dove? perché?）。
③ 角色扮演：你是博主，朋友（考官）采访你：「Perché fai video? Quanti follower hai?」。""",
             "points": 10,
             "rubric":
"""passato prossimo 使用正确；连接词（e, perché, ma）；描述图片用 presente；角色扮演能回应采访。满分 10，流利度/准确度/互动各约 3–4 分。""",
             "dims": [
                ("Pronuncia 发音", "发音清晰，重音基本正确"),
                ("Fluenza 流利度", "自我介绍流畅，含个人习惯与爱好"),
                ("Grammatica 语法", "现在时 / 近过去时使用基本正确"),
                ("Contenuto 内容", "涵盖自我介绍、图片描述、角色扮演三项任务"),
                ("Interazione 互动", "角色扮演用语得体，完成信息询问"),
             ],
             "ref":
"""Buongiorno, mi presento: mi chiamo Chiara, ho quindici anni e vivo a Bologna. Nel tempo libero uso i social network per ballare e pubblicare video su TikTok. Il mio video è diventato virale e ora ho molti follower! Nella foto vedo un ragazzo giovane che gira un video con il telefono in mano, davanti a un muro colorato, e sorride felice. Perché faccio video? Perché mi piace creare e far ridere le persone. Quanti follower ho? Più di centomila, grazie al mio cane!"""},
         ]},
    ],
})

# ============================== B1 =========================================
LEVELS.append({
    "code": "B1", "name": "CELI 2",
    "subtitle": "dipendenza dallo smartphone / cyberbullismo",
    "theme": "📱 数字时代、社交媒体与人工智能", "subj_max": 30,
    "audio": [
        {"title": "Testo 1 — Intervista", "body":
"""Giornalista: Dottor Bruni, cos'è la dipendenza da smartphone?
Bruni: È quando una persona non può stare senza telefono. Controlla i like ogni 5 minuti. Studi dicono che il 30% dei giovani è a rischio.
Giornalista: Cosa fare?
Bruni: Mettere il telefono lontano a tavola e prima di dormire. E fare sport."""},
        {"title": "Testo 2 — Storia", "body":
"""Mia cugina Sofia, 13 anni, riceveva messaggi cattivi su Instagram. Piangeva ogni sera. Poi ne ha parlato alla mamma e la scuola ha fermato i bulli. Ora sta bene."""},
        {"title": "Testo 3 — Annuncio", "body":
"""Campagna «Rete Amica»: numero verde 800123456 per le vittime di cyberbullismo. Tutti i giorni 9–20."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo A — Articolo breve", "body":
"""Secondo uno studio, i ragazzi guardano lo smartphone più di 4 ore al giorno. Molti controllano il telefono anche di notte. Questa dipendenza crea problemi a scuola e nelle relazioni. Gli esperti consigliano di spegnere il telefono un'ora prima di dormire."""},
            {"title": "Testo B — Email di una scuola", "body":
"""Gentile famiglia, domani alle 17:00 nella nostra scuola c'è un incontro sul cyberbullismo. Parleremo di come difendere i ragazzi dalle offese su internet. Vi aspettiamo."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Quante ore al giorno usano lo smartphone i ragazzi?", "options": ["A. meno di 2", "B. più di 4", "C. 10"], "answer": 1},
            {"type": "mc", "prompt": "2. Cosa consigliano gli esperti?", "options": ["A. usare il telefono di notte", "B. spegnerlo prima di dormire", "C. comprare un telefono nuovo"], "answer": 1},
            {"type": "match", "prompt": "3. Studio sulla dipendenza.", "options": ["A", "B"], "answer": 0},
            {"type": "match", "prompt": "4. Incontro sulla sicurezza.", "options": ["A", "B"], "answer": 1},
            {"type": "cloze", "text": "5. Il cyberbullismo è quando alcuni _____ mandano _____ cattivi su internet. La vittima ha _____ e non dice niente ai genitori.", "answers": ["bulli", "messaggi", "paura"]},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito 1 — Questionario（问卷，60–80 词）",
             "prompt": "Compila il questionario sull'uso dello smartphone: Nome / Età; Quante volte controlli il telefono al giorno?; Usi app per lo studio? (sì/no e perché); Il telefono ti aiuta o ti distrae? Scrivi 3–4 frasi (60–80 parole).",
             "limit": "60–80 词",
             "reference":
"""Nome: Luca, Età: 16. Controllo il telefono circa 30 volte al giorno. Uso app per lo studio, perché mi aiutano con le lingue. Il telefono a volte mi distrae, ma in generale mi aiuta. La sera studio con il tablet e ascolto musica per rilassarmi. Penso che il telefono sia utile se lo usiamo con moderazione."""},
            {"title": "Compito 2 — E-mail（给校长写邮件，120–150 词）",
             "prompt": "Scrivi al Dirigente scolastico. Racconta un caso di cyberbullismo subìto da te o da un compagno e chiedi aiuto. Inizia con \"Gentile Dirigente scolastico,\". 120–150 parole.",
             "limit": "120–150 词",
             "reference":
"""Gentile Dirigente scolastico, scrivo perché un mio compagno riceve messaggi offensivi su WhatsApp da alcuni studenti. Lui è molto triste e non vuole andare a scuola. Secondo me la scuola deve intervenire: serve un incontro con le famiglie e una regola chiara contro il cyberbullismo. La prego di aiutarci a fermare questa situazione e di proteggere gli studenti più fragili. Cordiali saluti, uno studente."""},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "1. Secondo Bruni, ogni quanti minuti controllano i like?", "options": ["A. 5", "B. 10", "C. 30"], "answer": 0},
            {"type": "mc", "prompt": "2. Che percentuale di giovani è a rischio?", "options": ["A. 10%", "B. 30%", "C. 50%"], "answer": 1},
            {"type": "mc", "prompt": "3. Cosa consiglia Bruni a tavola?", "options": ["A. usare il telefono", "B. metterlo lontano", "C. fare i compiti"], "answer": 1},
            {"type": "mc", "prompt": "4. Chi ha aiutato Sofia?", "options": ["A. la mamma e la scuola", "B. la polizia", "C. un amico"], "answer": 0},
            {"type": "mc", "prompt": "5. Su quale app riceveva messaggi Sofia?", "options": ["A. TikTok", "B. Instagram", "C. WhatsApp"], "answer": 1},
            {"type": "mc", "prompt": "6. Qual è il numero verde della campagna?", "options": ["A. 800123456", "B. 800654321", "C. 800111222"], "answer": 0},
            {"type": "mc", "prompt": "7. Qual è l'orario della campagna?", "options": ["A. 9–20", "B. 8–18", "C. 24 ore"], "answer": 0},
            {"type": "mc", "prompt": "8. Quanti anni ha Sofia?", "options": ["A. 11", "B. 13", "C. 15"], "answer": 1},
            {"type": "mc", "prompt": "9. Cosa fa Bruni nella vita?", "options": ["A. è un giornalista", "B. è un esperto/dottore", "C. è un bullo"], "answer": 1},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 自我介绍/兴趣/日常：Parla delle tue abitudini con il telefono。
② 描述图片：描述「一群青少年低头看手机」的图片，评论 dipendenza。
③ 角色扮演：你是 consigliere scolastico，向家长（考官）解释 come prevenire il cyberbullismo（用尊称 Lei）。""",
             "points": 25,
             "rubric":
"""passato prossimo / imperfetto 区分；condizionale（consiglierei）；描述用连接词；角色扮演用 formal "Lei"。满分 25，按流利/准确/互动评定。""",
             "dims": [
                ("Pronuncia 发音", "发音标准，语调节奏自然"),
                ("Fluenza 流利度", "连贯表达观点与习惯，少停顿"),
                ("Grammatica 语法", "现在时 / 近过去时 / imperfetto较准确，尝试复合句"),
                ("Contenuto 内容", "图片描述准确，角色扮演体现建议与预防"),
                ("Interazione 互动", "能用 formal 'Lei' 向家长解释，完成沟通"),
             ],
             "ref":
"""Buongiorno, mi chiamo Luca e ho sedici anni. Controllo il telefono circa trenta volte al giorno e lo uso soprattutto per studiare le lingue e parlare con gli amici. Nella foto vedo un gruppo di ragazzi seduti insieme, ma tutti guardano lo schermo del proprio telefono e non si parlano: è la dipendenza dallo smartphone. Come consigliere scolastico, spiego ai genitori che per prevenire il cyberbullismo serve parlare con i figli, controllare la privacy e segnalare subito i messaggi offensivi alla scuola."""},
         ]},
    ],
})

# ============================== B2 =========================================
LEVELS.append({
    "code": "B2", "name": "CELI 3",
    "subtitle": "intelligenza artificiale e lavoro / social e relazioni",
    "theme": "📱 数字时代、社交媒体与人工智能", "subj_max": 50,
    "audio": [
        {"title": "Testo 1 — Conferenza", "body":
"""Benvenuti. Oggi parliamo di IA e occupazione. Un rapporto dell'UE dice che entro il 2030 l'IA automatizzerà il 14% dei posti, ma creerà 11 milioni di nuovi lavori verdi e digitali. La sfida è la formazione. I Paesi che investono in istruzione soffrono meno. L'Italia deve correre."""},
        {"title": "Testo 2 — Dialogo su relazioni", "body":
"""— Marco, sei sempre sul telefono! Parliamo meno.
— Scusa, ma con i social resto in contatto con i miei amici lontani.
— Vero, però ieri non mi hai ascoltato mentre parlavo.
— Hai ragione. Metto via il telefono stasera, promesso."""},
        {"title": "Testo 3 — Servizio radio", "body":
"""Parliamo di cyberbullismo. Il 20% dei ragazzi tra 11 e 17 anni ha subìto offese online. Il 40% non ne parla con i genitori. Esiste un'app «Allerta» che segnala messaggi pericolosi. La legge punisce i colpevoli. La prevenzione parte dalla scuola."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo 1 — Articolo (IA e lavoro)", "body":
"""L'intelligenza artificiale sta cambiando il mondo del lavoro. Secondo l'OCSE, entro il 2030 circa il 14% dei posti di lavoro sarà completamente automatizzato, mentre un ulteriore 32% subirà modifiche profonde. Tuttavia, l'IA non sostituisce solo: crea nuove professioni, come l'addestratore di algoritmi. Le aziende cercano persone capaci di collaborare con le macchine, non di competere contro di esse."""},
            {"title": "Testo 2 — Intervista", "body":
"""«Non temo la tecnologia, ma la sua cattiva gestione», afferma la ricercatrice Elena Conti. «Il vero rischio non è perdere il lavoro, bensì perdere il senso del lavoro. La formazione continua è l'unica difesa seria»."""},
            {"title": "Testo 3 — Saggio breve (social e solitudine)", "body":
"""I social network promettono connessione, ma spesso producono solitudine. Studi dell'Università di Stanford mostrano che chi passa più di tre ore al giorno sui social ha livelli di ansia più alti. La relazione digitale è facile, immediata, ma superficiale: si «mettono like» senza ascoltare davvero."""},
            {"title": "Testo 4 — Commento", "body":
"""Non demonizziamo: i social permettono a chi è lontano di restare vicino. Il problema è l'uso, non lo strumento. Servono relazioni intenzionali, non automatiche."""},
            {"title": "Testo 5 — Quattro lavori con IA", "body":
"""A. Data ethicist: valuta l'impatto etico degli algoritmi. B. Prompt engineer: scrive istruzioni per IA generative. C. Tecnico robotica: ripara macchine in fabbrica. D. Social media manager: cura l'immagine online di un'azienda."""},
            {"title": "Testo 6 — Cinque affermazioni su social e relazioni", "body":
"""I. Le coppie oggi litigano anche per il tempo passato sul telefono. II. Molti conoscono partner online. III. I nonni usano meno i social dei nipoti. IV. Chi posta tanto spesso si sente solo. V. Le videochiamate aiutano le famiglie lontane."""},
            {"title": "Testo 7 — Inchiesta", "body":
"""Un sondaggio europeo rivela che il 60% dei lavoratori vorrebbe corsi di formazione sull'IA pagati dall'azienda. Solo il 20% li ha già. Il divario cresce tra chi sa usare gli strumenti e chi resta indietro."""},
         ],
         "items": [
            {"type": "mc", "prompt": "A.1-1. Secondo l'OCSE, entro il 2030 sarà automatizzato completamente…", "options": ["A. il 32%", "B. il 14%", "C. il 50%", "D. il 5%"], "answer": 1},
            {"type": "mc", "prompt": "A.1-2. Quale nuova professione nasce?", "options": ["A. l'autista", "B. l'addestratore di algoritmi", "C. il contadino", "D. il giornalista"], "answer": 1},
            {"type": "mc", "prompt": "A.1-3. Cosa cercano le aziende?", "options": ["A. chi compete con le macchine", "B. chi collabora con le macchine", "C. chi le spegne", "D. chi le vende"], "answer": 1},
            {"type": "mc", "prompt": "A.1-4. Elena Conti teme soprattutto…", "options": ["A. la tecnologia", "B. la cattiva gestione", "C. i giovani", "D. i sindacati"], "answer": 1},
            {"type": "mc", "prompt": "A.1-5. Qual è, per Conti, l'unica difesa seria?", "options": ["A. licenziare", "B. la formazione continua", "C. lo sciopero", "D. il telelavoro"], "answer": 1},
            {"type": "mc", "prompt": "A.1-6. Secondo Stanford, chi usa i social >3h ha…", "options": ["A. meno ansia", "B. più ansia", "C. più amici", "D. più soldi"], "answer": 1},
            {"type": "mc", "prompt": "A.1-7. La relazione digitale è definita…", "options": ["A. profonda", "B. superficiale/facile", "C. pericolosa", "D. inutile"], "answer": 1},
            {"type": "mc", "prompt": "A.1-8. Il commento sostiene che il problema è…", "options": ["A. lo strumento", "B. l'uso", "C. internet", "D. i giovani"], "answer": 1},
            {"type": "mc", "prompt": "A.1-9. Cosa servirebbe, secondo il commento?", "options": ["A. relazioni intenzionali", "B. niente social", "C. più like", "D. meno telefoni"], "answer": 0},
            {"type": "match", "prompt": "A.2-1. Scrive comandi per l'IA.", "options": ["A", "B", "C", "D"], "answer": 1},
            {"type": "match", "prompt": "A.2-2. Valuta l'etica.", "options": ["A", "B", "C", "D"], "answer": 0},
            {"type": "match", "prompt": "A.2-3. Ripara robot.", "options": ["A", "B", "C", "D"], "answer": 2},
            {"type": "match", "prompt": "A.2-4. Gestisce l'immagine web.", "options": ["A", "B", "C", "D"], "answer": 3},
            {"type": "match", "prompt": "A.2-5. Lavora con algoritmi e morale.", "options": ["A", "B", "C", "D"], "answer": 0},
            {"type": "match", "prompt": "A.2-6. Le coppie litigano per il telefono.", "options": ["Vero", "Falso", "Non detto"], "answer": 0},
            {"type": "match", "prompt": "A.2-7. Molti trovano l'amore online.", "options": ["Vero", "Falso", "Non detto"], "answer": 0},
            {"type": "match", "prompt": "A.2-8. I nonni usano più social dei giovani.", "options": ["Vero", "Falso", "Non detto"], "answer": 1},
            {"type": "match", "prompt": "A.2-9. Chi posta tanto è felice.", "options": ["Vero", "Falso", "Non detto"], "answer": 1},
            {"type": "match", "prompt": "A.2-10. Le videochiamate uniscono le famiglie.", "options": ["Vero", "Falso", "Non detto"], "answer": 0},
            {"type": "open", "prompt": "A.3-1. Qual è la percentuale di lavoratori che vorrebbe corsi sull'IA?", "ref": "Il 60%.", "rows": 2},
            {"type": "open", "prompt": "A.3-2. Qual è la percentuale che li ha già?", "ref": "Il 20%.", "rows": 2},
            {"type": "open", "prompt": "A.3-3. Cos'è il «divario» citato nel testo?", "ref": "Il divario tra chi sa usare gli strumenti e chi resta indietro.", "rows": 2},
            {"type": "open", "prompt": "A.3-4. Secondo te, chi deve pagare la formazione?", "ref": "L'azienda o lo Stato (risposta aperta).", "rows": 2},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "B.1 — Saggio breve / esperienza（二选一，120–180 词）",
             "prompt": "Scegli UNO: (a) Racconta un'esperienza in cui l'IA ti ha aiutato (o preoccupato) nel lavoro o nello studio. (b) Descrivi come i social hanno cambiato le tue relazioni con amici e familiari.",
             "limit": "120–180 词",
             "reference":
"""L'anno scorso ho usato un'IA per preparare un esame di statistica. All'inizio ero scettico, poi ho scoperto che spiegava gli esercizi meglio del libro. Mi ha fatto risparmiare tempo e ho preso un voto alto. Tuttavia mi ha anche preoccupato: se la macchina pensa per noi, impariamo meno? Ora la uso come aiuto, non come sostituto. Credo che l'IA nel lavoro sarà utile solo se restiamo padroni della tecnologia."""},
            {"title": "B.2 — Lettera / e-mail（三选一，80–100 词）",
             "prompt": "Scegli UNO: (a) Scrivi a un'amica per chiederle consiglio su un problema con i social. (b) Scrivi al datore di lavoro per proporre un corso di formazione sull'IA. (c) Scrivi un commento a un articolo sul cyberbullismo (opinione).",
             "limit": "80–100 词",
             "reference":
"""Gentile responsabile, propongo un corso di formazione sull'intelligenza artificiale per il nostro ufficio. Molti colleghi non conoscono questi strumenti e rischiano di restare indietro. Il corso aiuterebbe a lavorare meglio e più in fretta. Sono disponibile a organizzarlo con la direzione. Cordiali saluti."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""L'intelligenza artificiale sta cambiando _____ (1) modo _____ (2) cui lavoriamo. Molti _____ (3) dipendenti temono _____ (4) perdere _____ (5) posto, _____ (6) secondo gli esperti è _____ (7) opportunità _____ (8) formarsi. C'è _____ (9) bisogno _____ (10) imparare _____ (11) nuove tecnologie _____ (12) crescere.

_____ (13) social network sono nati per unire le persone, _____ (14) a volte le dividono. _____ (15) chi ne abusa rischia _____ (16) isolarsi. È importante fare _____ (17) uso consapevole: _____ (18) telefono non _____ (19) può sostituire _____ (20) abbraccio reale. _____ (21) combattere _____ (22) solitudine serve _____ (23) presenza vera.""",
            "answers": ["il","di","i","di","il","ma","un'","di","il","di","le","per","I","ma","Chi","di","un","il","può","un","Per","la","una"]},
         "rewrite": [
            {"prompt": "1. Ho un telefono. Il telefono è nuovo. Lo uso per studiare.", "ref": "Ho un telefono nuovo che uso per studiare."},
            {"prompt": "2. Lei posta foto. Le foto sono belle. Le posta ogni giorno.", "ref": "Lei posta ogni giorno belle foto."},
            {"prompt": "3. L'IA aiuta. Noi dobbiamo formarci. Altrimenti restiamo indietro.", "ref": "L'IA ci aiuta, ma dobbiamo formarci, altrimenti restiamo indietro."},
            {"prompt": "4. Il bullo ha offeso. La vittima ha pianto. La scuola è intervenuta.", "ref": "La vittima ha pianto perché il bullo l'ha offesa, ma la scuola è intervenuta."},
            {"prompt": "5. Uso i social. Perdo tempo. Devo stare attento.", "ref": "Uso i social, così perdo tempo; devo stare attento."},
            {"prompt": "6. Lui studia. Lui lavora. È stanco.", "ref": "Lui studia e lavora, perciò è stanco."},
            {"prompt": "7. L'app è utile. Costa poco. La consiglio.", "ref": "L'app è utile e costa poco, perciò la consiglio."},
         ],
         "wordform": [
            {"text": "1. Noi _____ (parlare) spesso al telefono.", "answers": ["parliamo"]},
            {"text": "2. L'IA _____ (diventare) importante per il lavoro.", "answers": ["è diventata"]},
            {"text": "3. Molti giovani sono _____ (dipendere) dallo smartphone.", "answers": ["dipendenti"]},
            {"text": "4. Le _____ (relazione) digitali sono veloci.", "answers": ["relazioni"]},
            {"text": "5. Sono _____ (preoccupato) per i ragazzi.", "answers": ["preoccupato"]},
            {"text": "6. Bisogna _____ (formare) i lavoratori.", "answers": ["formare"]},
            {"text": "7. Le notizie _____ (falso) si diffondono in rete.", "answers": ["false"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "D.1-1. Entro il 2030 l'IA automatizzerà…", "options": ["A. 5%", "B. 14%", "C. 30%", "D. 50%"], "answer": 1},
            {"type": "mc", "prompt": "D.1-2. Quanti nuovi lavori creerà?", "options": ["A. 1 milione", "B. 5 milioni", "C. 11 milioni", "D. 20 milioni"], "answer": 2},
            {"type": "mc", "prompt": "D.1-3. Qual è la sfida principale?", "options": ["A. il costo", "B. la formazione", "C. la politica", "D. il clima"], "answer": 1},
            {"type": "mc", "prompt": "D.1-4. Chi soffre meno?", "options": ["A. chi investe in istruzione", "B. chi non usa IA", "C. i giovani", "D. il nord"], "answer": 0},
            {"type": "mc", "prompt": "D.1-5. Cosa deve fare l'Italia?", "options": ["A. aspettare", "B. correre", "C. fermarsi", "D. esportare"], "answer": 1},
            {"type": "mc", "prompt": "D.1-6. Di cosa si lamenta l'amica?", "options": ["A. Marco studia", "B. Marco è sul telefono", "C. Marco esce", "D. Marco dorme"], "answer": 1},
            {"type": "mc", "prompt": "D.1-7. Perché Marco usa i social?", "options": ["A. per lavoro", "B. per amici lontani", "C. per giocare", "D. per soldi"], "answer": 1},
            {"type": "mc", "prompt": "D.1-8. Cosa non ha fatto Marco ieri?", "options": ["A. ascoltato l'amica", "B. mangiato", "C. risposto", "D. telefonato"], "answer": 0},
            {"type": "mc", "prompt": "D.1-9. Cosa promette Marco?", "options": ["A. comprare telefono", "B. mettere via il telefono", "C. uscire", "D. studiare"], "answer": 1},
            {"type": "mc", "prompt": "D.1-10. Dove mette il telefono?", "options": ["A. in tasca", "B. via/stasera", "C. in auto", "D. a scuola"], "answer": 1},
            {"type": "cloze", "text": "D.2-1. Il cyberbullismo colpisce i ragazzi tra 11 e _____ anni.", "answers": ["17"]},
            {"type": "cloze", "text": "D.2-2. La percentuale che subisce offese è il _____.", "answers": ["20%"]},
            {"type": "cloze", "text": "D.2-3. Il _____ % non parla con i genitori.", "answers": ["40"]},
            {"type": "cloze", "text": "D.2-4. Il nome dell'app è _____.", "answers": ["Allerta"]},
            {"type": "cloze", "text": "D.2-5. L'app segnala messaggi _____.", "answers": ["pericolosi"]},
            {"type": "cloze", "text": "D.2-6. La _____ punisce i colpevoli.", "answers": ["legge"]},
            {"type": "cloze", "text": "D.2-7. La prevenzione parte dalla _____.", "answers": ["scuola"]},
            {"type": "cloze", "text": "D.2-8. Le vittime hanno tra 11 e _____ anni.", "answers": ["17"]},
            {"type": "cloze", "text": "D.2-9. I messaggi sono definiti _____.", "answers": ["pericolosi"]},
            {"type": "cloze", "text": "D.2-10. La soluzione parte dalla _____ e dalla legge.", "answers": ["scuola"]},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 描述图片并回答：描述「ufficio con umani e robot che collaborano」图片，回答考官关于 IA e lavoro 的问题。
② 概述短文并回答：读一段关于 social e solitudine 的短文（100 词），用 3–4 句 riassunto，再讨论。
③ 情境角色扮演：你是 responsabile HR，向 dipendente（考官）spiega come l'IA cambierà il suo ruolo e proponi un corso。""",
             "points": 30,
             "rubric":
"""B2 要求论证清晰、语域正式（HR 情境用 Lei）、连接词丰富（tuttavia, pertanto, nonché）；riassunto 准确抓主旨。满分 30，按 内容/连贯/准确/互动 评定。""",
             "dims": [
                ("Pronuncia 发音", "发音标准，语域与场合匹配"),
                ("Fluenza 流利度", "表达连贯，能展开论述与评论"),
                ("Grammatica 语法", "虚拟 / 条件 / 关系代词较准确"),
                ("Contenuto 内容", "概述完整、立场清晰，论证有逻辑"),
                ("Interazione 互动", "HR 角色扮演说服力強，论证清晰"),
             ],
             "ref":
"""Buongiorno, sono il responsabile HR. Nella foto vedo un ufficio moderno dove due persone e un robot collaborano: l'uomo programma l'intelligenza artificiale e la macchina esegue i compiti ripetitivi, così risparmiamo tempo. Il testo sulla solitudine dice che i social promettono connessione ma spesso producono isolamento; secondo me servono relazioni intenzionali, non automatiche. Come HR spiego a lei che l'IA cambierà il suo ruolo: non la sostituirà, ma le chiederà di supervisionare le macchine. Pertanto proponiamo un corso di formazione per tutti i dipendenti."""},
         ]},
    ],
})

# ============================== C1 =========================================
LEVELS.append({
    "code": "C1", "name": "CELI 4",
    "subtitle": "algoritmi e democrazia / identità digitale",
    "theme": "📱 数字时代、社交媒体与人工智能", "subj_max": 50,
    "audio": [
        {"title": "Intervista — Costituzionalista", "body":
"""L'identità digitale è il nuovo certificato di cittadinanza. Senza SPID o CIE, oggi non accedi a sanità, fisco, voto online. Il rischio è l'esclusione: chi non ha competenze resta fuori dalla democrazia. Ma attenzione: centralizzare i dati crea un punto debole. Serve portabilità dei dati e diritto all'oblio. La democrazia digitale non è automatizzare il voto, è garantire che ognuno conti davvero."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo A — Saggio (registro formale)", "body":
"""Gli algoritmi che governano le nostre bacheche non sono neutri: incorporano scelte politiche e interessi economici. Quando una piattaforma decide cosa mostrarci, esercita una forma di potere invisibile. La democrazia presuppone cittadini informati; se l'informazione è filtrata da logiche di profitto, il dibattito pubblico si impoverisce. Non si tratta di censura esplicita, ma di una "visibilità diseguale" che favorisce ciò che genera click."""},
            {"title": "Testo B — Controargomento (tono polemico)", "body":
"""Chi grida all'algoritmo tiranno esagera. L'utente medio non è una vittima passiva: sceglie, ignora, disiscrive. La colpa non è del codice, ma della nostra pigrizia cognitiva. Restringere gli algoritmi per legge suona come paternalismo: meglio l'educazione critica che il controllo statale."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Secondo il Testo A, gli algoritmi sono…", "options": ["A. neutri", "B. portatori di scelte e interessi", "C. democratici", "D. gratuiti"], "answer": 1},
            {"type": "mc", "prompt": "2. La \"visibilità diseguale\" significa che…", "options": ["A. tutti vedono tutto", "B. il profitto favorisce certi contenuti", "C. non c'è censura", "D. lo Stato controlla"], "answer": 1},
            {"type": "mc", "prompt": "3. Il tono del Testo B è…", "options": ["A. accademico neutrale", "B. polemico/ironico", "C. poetico", "D. narrativo"], "answer": 1},
            {"type": "mc", "prompt": "4. Chi, per il Testo B, è responsabile?", "options": ["A. il codice", "B. la pigrizia dell'utente", "C. lo Stato", "D. le aziende"], "answer": 1},
            {"type": "tf", "prompt": "5. Il Testo A parla di censura esplicita.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "6. Il Testo B propone il controllo statale sugli algoritmi.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "7. Entrambi i testi parlano di democrazia e informazione.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "8. Il Testo A suggerisce che il dibattito pubblico soffre.", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito (a) — Riassunto（摘要，60–80 词）",
             "prompt": "Sintetizza le due posizioni dei testi letti in italiano corretto (tono accademico vs polemico, algoritmi e democrazia).",
             "limit": "60–80 词",
             "reference":
"""Il Testo A sostiene che gli algoritmi esercitano un potere invisibile e impoveriscono il dibattito pubblico filtrando l'informazione per profitto. Il Testo B obietta che l'utente è attivo e responsabile; auspica educazione critica anziché controllo statale. Le due posizioni divergono su causa (codice vs utente) e rimedio (regola vs formazione)."""},
            {"title": "Compito (b) — Saggio / articolo（议论文，140–170 词）",
             "prompt": "\"L'algoritmo minaccia o rafforza la democrazia?\" Sviluppa la tua tesi con argomenti e una riflessione sull'identità digitale.",
             "limit": "140–170 词",
             "reference":
"""L'algoritmo non è un giudice neutrale: decide, silenziosamente, cosa merita attenzione. In una democrazia, questo potere privato mina l'autodeterminazione dei cittadini. Tuttavia, il rimedio non è lo Stato che sostituisce il padrone, ma la trasparenza e l'alfabetizzazione digitale. L'identità digitale, poi, rischia di escludere chi resta analfabeta tecnologico: un diritto sulla carta, una barriera nella pratica. Serve portabilità dei dati e diritto all'oblio, perché la cittadinanza non si misura in clic."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""Gli algoritmi _____ (1) governano le nostre bacheche non _____ (2) affatto neutri: incorporano scelte _____ (3) cui non possiamo sottrarci. Se _____ (4) piattaforme decidessero in modo opaco, _____ (5) dibattito pubblico si impoverirebbe. È necessario _____ (6) i cittadini siano informati _____ (7) l'informazione non venga filtrata _____ (8) logiche di profitto. _____ (9) si tratta di una «visibilità diseguale» _____ (10) favorisce ciò _____ (11) genera clic, _____ (12) serve maggiore trasparenza.

L'identità digitale _____ (13) un nuovo certificato _____ (14) cittadinanza: senza SPID o CIE non _____ (15) accede _____ (16) sanità, fisco e voto. _____ (17) rischio è l'esclusione _____ (18) chi non ha competenze resta fuori _____ (19) democrazia. _____ (20) è necessario fare attenzione: centralizzare i dati crea _____ (21) punto debole. Serve _____ (22) portabilità dei dati _____ (23) diritto all'oblio.""",
            "answers": ["che","sono","a","le","il","che","affinché","da","Si","che","che","perciò","è","di","si","a","Il","di","dalla","Tuttavia","un","la","e"]},
         "rewrite": [
            {"prompt": "1. L'algoritmo filtra le notizie. L'utente non se ne accorge. Il dibattito si impoverisce.", "ref": "L'algoritmo filtra le notizie senza che l'utente se ne accorga, così il dibattito si impoverisce."},
            {"prompt": "2. La piattaforma decide cosa mostrare. Noi non possiamo intervenire. Serve una legge.", "ref": "Poiché la piattaforma decide cosa mostrare e noi non possiamo intervenire, serve una legge."},
            {"prompt": "3. L'utente è attivo. Sceglie e disiscrive. Il codice non è colpevole.", "ref": "Sebbene l'utente sia attivo, scelga e disiscriva, il codice non è colpevole."},
            {"prompt": "4. Centralizziamo i dati. Creiamo un punto debole. La sicurezza diminuisce.", "ref": "Centralizzando i dati creiamo un punto debole, per cui la sicurezza diminuisce."},
            {"prompt": "5. Il cittadino è informato. Difende i suoi diritti. La democrazia funziona.", "ref": "Se il cittadino è informato, difende i suoi diritti e la democrazia funziona."},
            {"prompt": "6. L'identità digitale esclude i deboli. Lo Stato deve garantire l'accesso. È una questione di giustizia.", "ref": "Poiché l'identità digitale esclude i deboli, lo Stato deve garantire l'accesso: è una questione di giustizia."},
            {"prompt": "7. L'IA automatizza i processi. I posti di lavoro cambiano. Dobbiamo formarci.", "ref": "Siccome l'IA automatizza i processi e i posti di lavoro cambiano, dobbiamo formarci."},
         ],
         "wordform": [
            {"text": "1. Se gli algoritmi _____ (essere, cong. imperf.) trasparenti, capiremmo le scelte.", "answers": ["fossero"]},
            {"text": "2. È urgente che il cittadino _____ (essere, cong.) informato.", "answers": ["sia"]},
            {"text": "3. La legge _____ (approvare, passivo) dal Parlamento.", "answers": ["è stata approvata"]},
            {"text": "4. Chi difende la libertà, _____ (lottare) per tutti.", "answers": ["lotta"]},
            {"text": "5. Non solo filtrano, _____ (ma anche / e anche) nascondono.", "answers": ["ma anche"]},
            {"text": "6. esercitare _____ (un potere / una potenza).", "answers": ["un potere"]},
            {"text": "7. _____ (Nonostante / Malgrado di) il rischio, serve formazione.", "answers": ["Nonostante"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "cloze", "text": "1. L'identità digitale è il nuovo certificato di _____.", "answers": ["cittadinanza"]},
            {"type": "cloze", "text": "2. Senza SPID o CIE non si accede a sanità, fisco e _____ online.", "answers": ["voto"]},
            {"type": "cloze", "text": "3. Il rischio è l'_____: chi non ha competenze resta fuori.", "answers": ["esclusione"]},
            {"type": "cloze", "text": "4. Servono _____ dei dati e diritto all'oblio.", "answers": ["portabilità"]},
            {"type": "tf", "prompt": "5. L'identità digitale è paragonata a un certificato di cittadinanza.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "6. Il voto online esiste già ovunque.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "7. Centralizzare i dati è sicuro secondo l'esperta.", "options": ["Vero", "Falso"], "answer": 1},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""带材料面试（长篇论述 + 深度讨论）。
Materiale: breve articolo su "algoritmi e polarizzazione politica"（120 词）。
Task：① 概述材料（2 分钟）；② 长篇论述：«L'IA minaccia o rafforza la democrazia?»（4 分钟）；③ 与考官深度讨论 identità digitale e diritti。""",
             "points": 25,
             "rubric":
"""C1 要求抽象论述、语域学术/正式、虚拟/条件娴熟、能应对质疑。满分 25，按 连贯/精确/深度/互动 评定。""",
             "dims": [
                ("Pronuncia 发音", "发音精准，语调节奏自如"),
                ("Fluenza 流利度", "长篇论述流畅，衔接自然"),
                ("Grammatica 语法", "虚拟 / 条件 / 被动准确，句式丰富"),
                ("Contenuto 内容", "立场明确，词汇丰富（transizione, precarietà, tutela）"),
                ("Interazione 互动", "深度讨论中回应质疑，逻辑自洽"),
             ],
             "ref":
"""La mia tesi è che l'algoritmo non è uno strumento neutrale, ma esercita un potere invisibile sul dibattito democratico. Come sostiene il Testo A, filtra l'informazione per profitto e impoverisce la discussione pubblica; il Testo B obietta che l'utente è attivo e responsabile, e auspica educazione critica anziché controllo statale. A mio avviso, tuttavia, la libertà individuale non basta se l'architettura stessa è manipolatoria. L'identità digitale rischia poi di escludere chi non ha competenze. Propongo trasparenza degli algoritmi, portabilità dei dati e diritto all'oblio, perché la cittadinanza non si misura in clic."""},
         ]},
    ],
})

# ============================== C2 =========================================
LEVELS.append({
    "code": "C2", "name": "CELI 5",
    "subtitle": "singolarità tecnologica / etica dell'IA",
    "theme": "📱 数字时代、社交媒体与人工智能", "subj_max": 50,
    "audio": [
        {"title": "Dibattito — Accademico", "body":
"""La singolarità è un orizzonte retorico, non una data. Chi la data al 2045 vende profezie, non scienza. Il punto vero è l'allineamento dei valori: un'IA potente ma non allineata ai diritti umani è un rischio reale, non fantascientifico. Servono standard vincolanti, non buoni propositi aziendali. E l'Europa deve guidare, non inseguire la Cina o gli USA."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo A — Saggio filosofico (registro alto)", "body":
"""La singolarità tecnologica non è un evento, è una metafora dello sgomento: immaginiamo una macchina che ci supera e, nel farlo, ci rende superflui. Ma forse il vero perturbante non è l'intelligenza artificiale che pensa, bensì la nostra che delega. Abbiamo esternalizzato il giudizio, come chi affida la bussola a chi non conosce la meta. L'etica dell'IA è, in fondo, l'etica della delega: decidere cosa non vogliamo più decidere."""},
            {"title": "Testo B — Editoriale (tono ironico/satirico)", "body":
"""«La macchina perfetta ci libererà dal lavoro, dalla scelta, dall'errore — insomma, dalla libertà.» Così recita il manifesto della nuova teologia siliconiana, dove il progresso è dogma e il dubbio eresia. Chi osa chiedere "a che prezzo?" viene tacciato di luddismo. E intanto, l'algoritmo ci sorride, ignaro di essere il nostro specchio."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. La \"singolarità\" è definita dall'autore come…", "options": ["A. un evento reale", "B. una metafora dello sgomento", "C. una vittoria", "D. un errore"], "answer": 1},
            {"type": "mc", "prompt": "2. La \"bussola\" nel Testo A rappresenta…", "options": ["A. la macchina", "B. il giudizio umano delegato", "C. il denaro", "D. la legge"], "answer": 1},
            {"type": "mc", "prompt": "3. Il tono del Testo B è…", "options": ["A. solenne", "B. ironico/satirico", "C. informativo", "D. lirico"], "answer": 1},
            {"type": "mc", "prompt": "4. \"Teologia siliconiana\" indica…", "options": ["A. una religione", "B. il culto del progresso tecnologico", "C. la scienza", "D. la politica"], "answer": 1},
            {"type": "tf", "prompt": "5. Secondo A, il vero problema è la macchina che pensa.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "6. B definisce il dubbio come \"eresia\" nel culto del progresso.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "7. Entrambi i testi criticano la delega di responsabilità all'IA.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "8. L'algoritmo, per B, è lo \"specchio\" dell'uomo.", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito 1 — Saggio / articolo（约 180–220 词）",
             "prompt": "«Singolarità tecnologica: mito, rischio o specchio dell'umano?» — 论述（约 180–220 词），引用 Testo A/B 的隐喻与反讽。",
             "limit": "180–220 词",
             "reference":
"""La singolarità tecnologica, come nota il nostro autore, è meno un evento che una "metafora dello sgomento": temiamo non la macchina che pensa, ma la nostra resa al pensiero altrui. Il manifesto "siliconiano" che la seconda voce irride rivela una teologia del progresso dove il dubbio è eresia e la libertà, paradossalmente, il primo lusso sacrificato sull'altare dell'efficienza. Se delegare il giudizio è esternalizzare la bussola, l'etica dell'IA smette di essere tecnica e diventa politica: decidere ciò che rifiutiamo di decidere. Non serve aspettare il 2045; la delega è già qui, quotidiana, invisibile."""},
            {"title": "Compito 2 — Policy brief（政策建议，70–90 词）",
             "prompt": "Scrivi un breve contributo a un ente di ricerca (70–90 词): propone 3 principi di etica dell'IA.",
             "limit": "70–90 词",
             "reference":
"""Raccomandiamo all'ente: 1) adottare standard vincolanti di "allineamento ai diritti umani"; 2) garantire trasparenza e audit pubblici degli algoritmi; 3) istituire un diritto alla spiegazione per ogni decisione automatizzata. L'innovazione senza questi tre principi non è progresso, è abdicazione."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""La singolarità tecnologica è _____ (1) orizzonte retorico, non _____ (2) data: _____ (3) la data al 2045 vende profezie, non scienza. Il punto _____ (4) è l'allineamento dei valori; un'IA potente, _____ (5) non allineata ai diritti umani, è _____ (6) rischio reale. _____ (7) servono standard vincolanti, _____ (8) buoni propositi aziendali. _____ (9) l'Europa deve guidare, _____ (10) inseguire la Cina _____ (11) gli USA. _____ (12) si tratta di etica, non di fantascienza.

Delegare _____ (13) giudizio è esternalizzare _____ (14) bussola morale: _____ (15) che l'etica dell'IA diventa politica. _____ (16) la macchina decidesse meglio _____ (17) noi, _____ (18) resteremmo padroni _____ (19) scelta? Tale _____ (20) è _____ (21) abdicazione _____ (22) non è progresso, _____ (23) resa al pensiero altrui.""",
            "answers": ["un","una","chi","vero","pur","un","Perciò","non","Inoltre","non","o","Si","il","la","è","Se","di","ne","della","Quest'","un'","ma","bensì"]},
         "rewrite": [
            {"prompt": "1. La macchina pensa. Noi temiamo la nostra resa. Il dubbio è eresia.", "ref": "Non temiamo la macchina che pensa, ma la nostra resa, poiché il dubbio è eresia."},
            {"prompt": "2. Il manifesto irride la teologia del progresso. La libertà è sacrificata. L'efficienza è l'altare.", "ref": "Il manifesto irride la teologia del progresso in cui la libertà è sacrificata sull'altare dell'efficienza."},
            {"prompt": "3. L'IA è potente. Non è allineata ai diritti. È un rischio reale.", "ref": "Sebbene l'IA sia potente, non è allineata ai diritti, perciò è un rischio reale."},
            {"prompt": "4. L'Europa guida. Non insegue la Cina. Non insegue gli USA.", "ref": "L'Europa deve guidare, anziché inseguire la Cina o gli USA."},
            {"prompt": "5. Deleghiamo il giudizio. Esternalizziamo la bussola. L'etica diventa politica.", "ref": "Delegando il giudizio, esternalizziamo la bussola, sicché l'etica diventa politica."},
            {"prompt": "6. La singolarità è un orizzonte. Non è una data. Chi la data vende profezie.", "ref": "La singolarità è un orizzonte, non una data: chi la data vende profezie, non scienza."},
            {"prompt": "7. La delega è quotidiana. È invisibile. Non serve aspettare il 2045.", "ref": "Poiché la delega è quotidiana e invisibile, non serve aspettare il 2045."},
         ],
         "wordform": [
            {"text": "1. Se l'IA _____ (avere, cong. imperf.) coscienza, ne discuteremmo.", "answers": ["avesse"]},
            {"text": "2. Pur _____ (sapere, gerundio) i rischi, proseguono.", "answers": ["sapendo"]},
            {"text": "3. Non appena _____ (essere, fut.) pronta, la legge entrerà in vigore.", "answers": ["sarà"]},
            {"text": "4. delega → aggettivo: _____ (delegabile / delegato).", "answers": ["delegabile"]},
            {"text": "5. etica → avverbio di registro alto: _____ (eticamente).", "answers": ["eticamente"]},
            {"text": "6. esercitare una _____ (sorta / specie) di potere invisibile.", "answers": ["sorta"]},
            {"text": "7. «a che prezzo» richiede una risposta di tipo _____ (retorico / reale).", "answers": ["retorico"]},
            {"text": "8. Chi delega il giudizio _____ (a / da) altri ne è responsabile.", "answers": ["a"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "1. L'ospite considera la singolarità…", "options": ["A. una data certa", "B. un orizzonte retorico", "C. un errore", "D. una legge"], "answer": 1},
            {"type": "mc", "prompt": "2. Chi \"data al 2045\"?", "options": ["A. scienziati seri", "B. chi vende profezie", "C. l'Europa", "D. la Cina"], "answer": 1},
            {"type": "mc", "prompt": "3. Il vero rischio è…", "options": ["A. la fantascienza", "B. IA non allineata ai diritti", "C. il costo", "D. il clima"], "answer": 1},
            {"type": "mc", "prompt": "4. Cosa serve secondo l'ospite?", "options": ["A. buoni propositi", "B. standard vincolanti", "C. pubblicità", "D. silenzio"], "answer": 1},
            {"type": "mc", "prompt": "5. Quale ruolo per l'Europa?", "options": ["A. inseguire", "B. guidare", "C. uscire", "D. aspettare"], "answer": 1},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""抽象话题演讲 + 批判性质疑回应。
Task：① 演讲（4–5 分钟）「La singolarità tecnologica è il nostro specchio, non il nostro padrone」；② 考官提出质疑（es. «Ma se la macchina decide meglio di noi?»），考生批判性回应；③ 结语 su etica dell'IA e responsabilità umana。""",
             "points": 25,
             "rubric":
"""C2 要求高度抽象、语域学术文学、隐喻运用、虚拟/条件/被动娴熟、能机敏回应质疑并深化论点。满分 25，按 精确/深度/流畅/批判互动 评定。""",
             "dims": [
                ("Pronuncia 发音", "发音精准，学术语域自如"),
                ("Fluenza 流利度", "演讲连贯，抽象概念流转自然"),
                ("Grammatica 语法", "复杂句法准确（虚拟 / 条件 / 被动 / 关系）"),
                ("Contenuto 内容", "抽象概念清晰，词汇精准（agency, rendita, soggettività）"),
                ("Pensiero critico 思辨", "批判性回应质疑，逻辑自洽有深度"),
             ],
             "ref":
"""La mia tesi è che la singolarità tecnologica è il nostro specchio, non il nostro padrone. Come scrive il nostro autore, non temiamo la macchina che pensa, ma la nostra resa al pensiero altrui: delegare il giudizio è esternalizzare la bussola morale. Il manifesto della «teologia siliconiana» irride chi osa chiedere a che prezzo, sacrificando la libertà sull'altare dell'efficienza. Se la macchina decidesse meglio di noi, resteremmo comunque padroni della scelta? A chi obietta che l'IA ci libererà, rispondo: la vera etica è decidere ciò che non vogliamo più decidere. L'innovazione senza diritti umani non è progresso, è abdicazione."""},
         ]},
    ],
})

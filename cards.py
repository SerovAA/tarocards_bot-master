import sqlite3


def init_db():
    """
    Initializes the database, creating tables
    and inserting cards if they don't exist.
    """
    with sqlite3.connect('tarocards.db') as connection:
        create_tables(connection)

        insert_cards(connection, 'old_cards', tarot_cards)
        insert_cards(connection, 'new_cards', tarot_cards_jr)


def insert_cards(connection, table_name: str, cards: list[tuple[str, str, str]]):
    """
    Inserts cards into the specified table if they don't already exist.

    Args:
        connection (sqlite3.Connection): The database connection.
        table_name (str): The name of the table to insert into.
        cards (list[tuple[str, str, str]]): List of card tuples (name, description, url).
    """
    with connection:
        cursor = connection.cursor()
        for card in cards:
            name, description, url = card
            cursor.execute(f"SELECT name FROM {table_name} WHERE name = ?", (name,))
            if not cursor.fetchone():
                cursor.execute(f'''
                    INSERT INTO {table_name} (name, description, url)
                    VALUES (?, ?, ?)
                ''', (name, description, url))


def create_tables(connection):
    """
    Creates the necessary tables in the database if they don't exist.

    Args:
        connection (sqlite3.Connection): The database connection.
    """
    with connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS old_cards (
                card_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                description TEXT,
                url TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS new_cards (
                card_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                description TEXT,
                url TEXT
            )
        ''')


tarot_cards = [
    ('Шут', 'Новое начало, приключение, неизвестность.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/RWS_Tarot_00_Fool.jpg/220px-RWS_Tarot_00_Fool.jpg'),
    ('Маг', 'Сила воли, мастерство, создание.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/RWS_Tarot_01_Magician.jpg/220px-RWS_Tarot_01_Magician.jpg'),
    ('Верховная Жрица', 'Интуиция, тайна, подсознание.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/RWS_Tarot_02_High_Priestess.jpg/220px-RWS_Tarot_02_High_Priestess.jpg'),
    ('Императрица', 'Плодородие, изобилие, творчество.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/RWS_Tarot_03_Empress.jpg/220px-RWS_Tarot_03_Empress.jpg'),
    ('Император', 'Власть, структура, контроль.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/RWS_Tarot_04_Emperor.jpg/220px-RWS_Tarot_04_Emperor.jpg'),
    ('Верховный Жрец', 'Традиция, образование, духовность.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/RWS_Tarot_05_Hierophant.jpg/220px-RWS_Tarot_05_Hierophant.jpg'),
    ('Влюблённые', 'Любовь, партнерство, выбор.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/RWS_Tarot_06_Lovers.jpg/220px-RWS_Tarot_06_Lovers.jpg'),
    ('Колесница', 'Сила воли, победа, уверенность.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/RWS_Tarot_07_Chariot.jpg/220px-RWS_Tarot_07_Chariot.jpg'),
    ('Сила', 'Мужество, сила, терпение.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/RWS_Tarot_08_Strength.jpg/220px-RWS_Tarot_08_Strength.jpg'),
    ('Отшельник', 'Одиночество, мудрость, поиск.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/RWS_Tarot_09_Hermit.jpg/220px-RWS_Tarot_09_Hermit.jpg'),
    ('Колесо Фортуны', 'Удача, цикл, судьба.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg/220px-RWS_Tarot_10_Wheel_of_Fortune.jpg'),
    ('Справедливость', 'Справедливость, равновесие, истина.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/RWS_Tarot_11_Justice.jpg/220px-RWS_Tarot_11_Justice.jpg'),
    ('Повешенный', 'Жертва, отречение, новое видение.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/RWS_Tarot_12_Hanged_Man.jpg/220px-RWS_Tarot_12_Hanged_Man.jpg'),
    ('Смерть', 'Изменение, конец, новое начало.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/RWS_Tarot_13_Death.jpg/220px-RWS_Tarot_13_Death.jpg'),
    ('Умеренность', 'Умеренность, баланс, гармония.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/RWS_Tarot_14_Temperance.jpg/220px-RWS_Tarot_14_Temperance.jpg'),
    ('Дьявол', 'Искушение, привязанность, тьма.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/RWS_Tarot_15_Devil.jpg/220px-RWS_Tarot_15_Devil.jpg'),
    ('Башня', 'Разрушение, перемены, освобождение.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/RWS_Tarot_16_Tower.jpg/220px-RWS_Tarot_16_Tower.jpg'),
    ('Звезда', 'Надежда, вдохновение, вера.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/RWS_Tarot_17_Star.jpg/220px-RWS_Tarot_17_Star.jpg'),
    ('Луна', 'Иллюзия, страхи, тайна.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/RWS_Tarot_18_Moon.jpg/220px-RWS_Tarot_18_Moon.jpg'),
    ('Солнце', 'Радость, успех, просветление.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/RWS_Tarot_19_Sun.jpg/220px-RWS_Tarot_19_Sun.jpg'),
    ('Суд', 'Оценка, возрождение, карма.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/RWS_Tarot_20_Judgement.jpg/220px-RWS_Tarot_20_Judgement.jpg'),
    ('Мир', 'Завершение, успех, интеграция.',
     'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/RWS_Tarot_21_World.jpg/220px-RWS_Tarot_21_World.jpg')
]

tarot_cards_jr = [
    ("Туз жезлов",
     "Карта сигнализирует о том, что пора набраться смелости и начать двигаться к своей мечте. Доверьтесь интуиции и начните реализовывать творческие идеи. Инстинкты подскажут, в правильном ли направлении вы идете. Вероятно, вы ждали знака, который подтвердил бы тот факт, что вам пора сделать первый шаг к цели. Туз Жезлов он и есть!",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Wands01.jpg/345px-Wands01.jpg?20240404235445"),
    ("Двойка жезлов",
     "Пришло время двигаться вперед. Наверняка у вас есть мечты и цели. Подготовьте четкий план и следуйте ему. Сначала вам будет трудно, так как придется выбраться из зоны комфорта, но не стоит отступать. Карта Таро Двойка Жезлов говорит о том, что в конце пути вас ждет успех. Вы преодолеете все препятствия.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Wands02.jpg/348px-Wands02.jpg?20240404235826"),
    ("Тройка жезлов",
     "Вы обрели твердую почву под ногами благодаря собственным действиям. Вероятно, вы потратили достаточно времени, чтобы составить четкий план на будущее, и уже делаете первые шаги навстречу своим целям. Ситуация полностью под вашим контролем. Скоро вы заметите, что у вас куда больше возможностей, чем вы думали. Но иногда придется выходить из зоны комфорта. Например, уйти из дома или отправиться в путешествие, где вы столкнетесь с новыми обстоятельствами.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wands03.jpg/344px-Wands03.jpg?20240404235907"),
    ("Четверка жезлов",
     "Карта сигнализирует, что скоро тот, кому она выпала, обретет счастье и стабильность. Ему наконец-то удастся достичь баланса, к которому он так долго стремился. Сейчас самое время встретиться с близкими людьми. Не обязательно ждать повода для этого. Лучше отдать предпочтение домашней обстановке.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Wands04.jpg/346px-Wands04.jpg?20240405000110"),
    ("Пятерка жезлов",
     "Карта Таро Пятерка Жезов указывает на конфликт в группе людей. Он может быть связан как с семьей, так и с работой. Участники беседы не желают слушать друг друга, каждый лишь пытается высказать свою точку зрения, и это усугубляет ситуацию. Вам необходимо сделать шаг к примирению, постарайтесь сделать так, чтобы каждый имел возможность объясниться.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Wands05.jpg/346px-Wands05.jpg?20240405000139"),
    ("Шестерка жезлов",
     "Карта Таро Шестерка Жезлов говорит о том, что благодаря упорству и таланту вам удалось добиться всех поставленных целей. Вы также получили общественное признание, окружающие заметили ваши достижения. Однако относитесь к славе с осторожностью. Похвалы могут превратить вас в высокомерного эгоиста. А таких персонажей не слишком любят.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Wands06.jpg/349px-Wands06.jpg?20240405000206"),
    ("Семерка жезлов",
     "Вы стремительно двигаетесь к своей цели и уже добились каких-то высот. Чтобы сохранить положение, вам необходимо преодолеть препятствия. Будьте готовы к столкновению с конкурентами. Многие мечтают достичь тех же результатов, что и вы. Никому не позволяйте занять ваше место. Если вы будете преданы своим мечтам, то сможете справиться с любыми проблемами.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wands07.jpg/346px-Wands07.jpg?20240405000247"),
    ("Восьмерка жезлов",
     "Трудности остались позади. Впереди вас ждет светлое будущее. Будьте готовы к переменам. Открывшиеся возможности могут быть связаны как с карьерой, так и с отношениями. Но наберитесь терпения. Жизнь не изменится за секунду.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Wands08.jpg/348px-Wands08.jpg?20240405000315"),
    ("Девятка жезлов",
     "Вероятно, вы преодолели немало трудностей, однако препятствия на вашем пути еще не закончились. Не стоит отчаиваться. Карта сигнализирует о том, что еще есть надежда на успех. Главное не сдаваться, осталось сделать последний шаг.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Tarot_Nine_of_Wands.jpg/348px-Tarot_Nine_of_Wands.jpg?20240405000910"),
    ("Десятка жезлов",
     "Вы потратили много ресурсов и энергии на преодоление препятствий на своем жизненном пути. К счастью, старания были вознаграждены, и вы получили то, что хотели. Однако не время расслабляться. Теперь вам необходимо поддерживать репутацию. Например, следить за процветающим бизнесом и не дать ему разориться. Карта рекомендует правильно расставить приоритеты и морально подготовиться к тому, что в вашей жизни могут появиться проблемы.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wands10.jpg/344px-Wands10.jpg?20240405001007"),
    ("Паж жезлов",
     "Паж очень любопытен, он желает достичь успеха и знает, что для этого необходимо сделать. Однако из-за неопытности и страха некоторые его идеи остаются нереализованными. Герой карты Таро Паж Жезлов постоянно в поисках чего-то нового, но он рассеян и легко отвлекается. Ему необходимо научиться контролировать себя и концентрироваться.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Wands11.jpg/346px-Wands11.jpg?20240405001051"),
    ("Рыцарь жезлов",
     "Тот, кому выпала эта карта, полон сил и энергии. Их необходимо потратить на воплощение желаний. Вероятно, этот человек хочет произвести впечатление на окружающих своими знаниями и навыками и получить признание со стороны. Рыцарь Жезлов также сигнализирует о том, что пришло время путешествовать, поменять работу или переехать. Несмотря на зашкаливающий энтузиазм, не принимайте спонтанные решения. Составьте четкий план действий и оцените риски.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Wands12.jpg/348px-Wands12.jpg?20240405001121"),
    ("Королева жезлов",
     "Королева смела и энергична, она готова сражаться не только за себя, но и за своих близких, хотя иногда бывает и эгоцентричной. Карта Таро говорит о том, что вы добьетесь успеха на работе за короткий промежуток времени. Вероятно, женщина сыграет важную роль в вашем карьерном росте.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Wands13.jpg/349px-Wands13.jpg?20240405001151"),
    ("Король жезлов",
     "Король Жезлов — прирожденный лидер, он легко взаимодействует с людьми и ловко раздает команды. Как только такой человек поставит себе цель, он будет неотступно двигаться к ней. Ему не страшны испытания, благодаря им герой карты может почувствовать прилив адреналина.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Wands14.jpg/345px-Wands14.jpg?20240405001226"),

    ("Туз кубков",
     "Туз Кубков – это знак внутренней энергии, открытости души ко всему новому, душевной гармонии и комфорта. Одним словом можно сказать, что это карта блаженства. Выпадающий в раскладе такой Аркан указывает на то, что счастье стоит у дверей гадающего. Это светлый луч, появляющийся в темной душе, он выдворяет оттуда всю печаль, уныние, злость, страхи.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Cups01.jpg/347px-Cups01.jpg?20240405001848"),
    ("Двойка кубков",
     "Аркан свидетельствует о взаимной симпатии, перспективных связях, успешном сотрудничестве, мире, который наконец-то случается после длительных ссор и размолвок. Обязательно в жизни человека произойдут радостные события и встречи.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Cups02.jpg/346px-Cups02.jpg?20240405001924"),
    ("Тройка кубков",
     "Карта символизирует, как правило, время радости, праздника. В любовных и дружеских отношениях будет полное взаимопонимание между партнерами. Все запланированные дела увенчаются успехом. Аркан дает подсказку гадающему человеку, что сейчас наступает благоприятное время, чтобы восстановить отношения со старыми друзьями, родственниками, ведь наступает светлая полоса в жизни.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Cups03.jpg/349px-Cups03.jpg?20240405002001"),
    ("Четверка кубков",
     "Человек, которому выпал в раскладе такой Аркан, упускает большие возможности в своей жизни. Это происходит по причине того, что он слишком эгоистичен, заносчив, горд, считая себя излишне умным. Он обижен на многих людей, недоволен собой, что выражается в постоянном процессе самоанализа. Это создает большое количество комплексов и страхов.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Cups04.jpg/349px-Cups04.jpg?20240405002051"),
    ("Пятерка кубков",
     "Аркан говорит о разочаровании, неожиданных неприятностях, меланхолии, печали, боли, скорби об утраченном. Возможно, у человека произойдет состояние сожаления из-за того, что его мечты и желания не осуществились, хотя он так на это рассчитывал.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Cups05.jpg/350px-Cups05.jpg?20240405002127"),
    ("Шестерка кубков",
     "Аркан означает внутреннюю гармонию, великодушие и щедрость. В действительности, карта отвечает за позитивное проявление. Можно считать, что все невзгоды уже в прошлом, а теперь только благополучие. Как только трудности отступили, человек вновь начинает мечтать и строить планы, довольствуется спокойствием и успехами своих трудов.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Cups06.jpg/348px-Cups06.jpg?20240405002214"),
    ("Семерка кубков",
     "Основное значение карты заключается в том, что каждый выбор, над которым гадающий раздумывает, уже предопределен судьбой, то есть сам факт выбора – иллюзия, обман. Кроме того, карта может трактоваться и как ошибочный выбор, который не несет ничего хорошего в себе. Указывает Аркан в некоторых случаях и на то, что вариантов слишком много, сложно определиться, прийти к единственно верному решению.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Cups07.jpg/346px-Cups07.jpg?20240405002302"),
    ("Восьмерка кубков",
     "Выпадает карта, как правило, человеку, который ищет по жизни все больше новых благ, при этом они все у него перед носом. Часто карта символизирует отказ от мирского вследствие разочарования, переходного периода. В итоге начинается поиск духовного пути.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Cups08.jpg/348px-Cups08.jpg?20240405002401"),
    ("Девятка кубков",
     "Если в раскладе выпадает эта карта, то в будущем ожидает успех в материальном плане, хороший достаток. Наступает светлая полоса, эмоциональное удовольствие, а также интеллектуальное. Здоровью не угрожают никакие проблемы. Любые цели, которые намечаются, могут воплотиться в жизнь.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Cups09.jpg/348px-Cups09.jpg?20240405002511"),
    ("Десятка кубков",
     "Десятка кубков символизирует счастливую и гармоничную семейную жизнь. Счастье будет продолжительным, принесет массу положительных эмоций. Человек, делающий расклад, добьется многого в духовной сфере, отчего испытает неописуемую радость. Все дела будут благополучно завершены. Карта может предзнаменовать начало какого-то нового этапа в жизни, что принесет с собой душевное спокойствие и гармонию.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Cups10.jpg/346px-Cups10.jpg?20240405002536"),
    ("Паж кубков",
     "Аркан наделен тихой радостью, романтикой, мечтой и грезами. Карта несет эмоциональную нагрузку и является символом любви. При раскладе стоит ожидать любовного послания, известия о свадьбе, возможно, придет информация о беременности или рождении ребенка.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Cups11.jpg/348px-Cups11.jpg?20240405002636"),
    ("Рыцарь кубков",
     "Какими качествами обладает рыцарь? Конечно же, романтичность, сердечность, целеустремленность. Если расклад делается на характер человека, именно эти качества будут описывать его натуру. Он верен своим принципам и идеалам, всегда следует за мечтой, очень чуток и тактичен.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Cups12.jpg/346px-Cups12.jpg?20240405002710"),
    ("Королева кубков",
     "Королева Кубков символизирует успех в задуманных делах при помощи гениальной интуиции. В жизни человека, которому выпала эта карта, вообще есть ощущение постоянного предчувствия, словно дар ясновидения.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Cups13.jpg/348px-Cups13.jpg?20240405002738"),
    ("Король кубков",
     "Эта карта предвещает утешение, поддержку и обретение защиты. Король Кубков (Чаш) в младшем аркане Таро — это не просто друг, готовый выслушать и дать мудрый совет, но также символ человека с особым характером. Обычно появление Короля Кубков указывает на наличие в жизни определённого человека, который обладает особым характером и может сыграть важную роль в конкретной ситуации.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Cups14.jpg/350px-Cups14.jpg?20240405002811"),

    ("Туз мечей",
     "Эта карта Таро символизирует торжество разума и ясность мысли. В прямом положении она означает прозрачное видение ситуации и возможность принять верное решение. Особенностью данного аркана является то, что ум здесь проявляется в более чистой, неотягощенной форме. Ему часто противопоставляют «2 Шпаг», которая символизирует разум, затуманенный сомнениями.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Swords01.jpg/346px-Swords01.jpg?20240406051351"),
    ("Двойка мечей",
     "Карта символизирует двойственность, смятения, выбор, который становится мукой из-за постоянных сомнений. Она говорит о том, что человек направляет огромную часть своей энергии на то, чтобы найти ответ с помощью логики, однако решение придет лишь тогда, когда вопрошающий откроет сердце и прислушается к интуиции. Это может быть нелегко, поскольку сознание и подсознание оказались разделены: об этом говорят изображения луны и моря.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Swords02.jpg/350px-Swords02.jpg?20240406051541"),
    ("Тройка мечей",
     "В Таро значение карты «3 Мечей» часто ассоциируется с противоречием. Это может быть несчастная любовь, где чувства спорят с разумом, или ограничения воплощения мечты, связанные с несоответствием желаний и возможностей. Аркан может также означать слабость характера или же наоборот: толкование зависит от сопутствующих карт и от самого вопроса.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Swords03.jpg/344px-Swords03.jpg?20240406051634"),
    ("Четверка мечей",
     "Значение карты Таро «4 Мечей» связано с покоем. Причем отсутствие действий здесь вынужденное: приостановление карьерного роста, затруднения. Этот аркан часто указывает на период застоя в судьбе человека. Он во многом напоминает «Повешенного», но в отличие от него всегда указывает на понятные вещи и не требует переворота духовных ценностей.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Swords04.jpg/349px-Swords04.jpg?20240406051710"),
    ("Пятерка мечей",
     "Это одна из самых неблагоприятных карт в раскладе. Она символизирует продолжительную черную полосу в судьбе человека, говорит о болезненном конфликте, скандале и унижении. При этом аркан не указывает на роль вопрошающего в этой ситуации: он может быть как жертвой, так и источником негатива.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Swords05.jpg/346px-Swords05.jpg?20240406051738"),
    ("Шестерка мечей",
     "В картах Таро «6 Мечей» имеет значение перемен, смены положения или переезда. Однако она не говорит, будет корректировка обстоятельств положительной или отрицательной. Здесь все зависит от настроя вопрошающего. Относительно других арканов «6 Шпаг» имеет промежуточное прочтение между «Колесницей», обозначающей радостное событие, и «8 Кубков», говорящей о печальном расставании.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Swords06.jpg/347px-Swords06.jpg?20240406051835"),
    ("Семерка мечей",
     "Аркан отражает подлость, обман, лицемерие, хитрость и интриги. Это может быть злословие, сплетни, высокомерное поведение или отказ от ответственности по принципу «моя хата с краю». Хотя данная карта визуально напоминает «Мага» (характеризующего ясность ума), они имеют диаметрально противоположное толкование.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Swords07.jpg/348px-Swords07.jpg?20240406051911"),
    ("Восьмерка мечей",
     "Отражает препятствия, которые ставит на своем пути сам человек. Часто значение карты Таро «8 Мечей» говорит о внутренних барьерах, подавлении части личности на уровне подсознания. При этом человек вводит себя в заблуждение, пытаясь найти причину своих трудностей вовне: «Я бы отправился в путешествие, но…», «Я бы прошла этот курс, но…» и так далее.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Swords08.jpg/348px-Swords08.jpg?20240406051937"),
    ("Девятка мечей",
     "Она символизирует сожаление, осознание печальной новости и терзания совести. Значение карты Таро «9 Мечей» исходит из описания аркана: человек сидит на кровати, закрыв глаза, и не может уснуть из-за мучительных мыслей. Изображение может говорить о совершении постыдного поступка, сложном испытании или реальной угрозе жизни. Причем в одиночку карта не раскрывает, что именно стало причиной беспокойства, тоски, отчаяния, а лишь указывает на эти чувства.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Swords09.jpg/348px-Swords09.jpg?20240406052007"),
    ("Десятка мечей",
     "Она символизирует конец. Это может быть финал отношений, увольнение, разрыв связей, словом, завершение какого-то периода. Часто указывает на болезненный конец, однако количество клинков говорит о торжестве разума в этой ситуации. Толкование аркана можно сопоставить со «Смертью», однако здесь речь идет не о естественном завершении цикла, а о внезапном преждевременном финале.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Swords10.jpg/345px-Swords10.jpg?20240406052050"),
    ("Паж мечей",
     "Имеет обозначение открывшихся возможностей, нового взгляда на привычные вещи, пробуждения, свежего импульса. Аркан часто указывает на прояснение ситуации, получение свежих необходимых знаний, благодаря которым даже самая запутанная история становится понятной.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Swords11.jpg/346px-Swords11.jpg?20240406052117"),
    ("Рыцарь мечей",
     "Несет обострение отношений, раздор. Аркан указывает на споры, конфликты, холод даже в тех сферах, которые прежде олицетворяли уют, надежность и покой. Нередко из-за этого холода на поверхность выходят все затаившиеся обиды и претензии. В прямом положении в раскладе он означает негатив.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Swords12.jpg/347px-Swords12.jpg?20240406052151"),
    ("Королева мечей",
     "Символизирует интеллект, независимость, творчество и открытость. Данный аркан говорит о женском проявлении стихии воздуха и указывает на решение поставленных задач при помощи логики и постоянного совершенствования разума. Все сомнения при этом отступают прочь.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Swords13.jpg/345px-Swords13.jpg?20240406052222"),
    ("Король мечей",
     "Она символизирует ум и высокий интеллект. Стихия воздуха здесь имеет мужской характер, проявляется в творчестве, хитрости и настойчивости. В раскладах на решение проблем это часто означает тщательный анализ ситуации, расчетливый подход, необходимость действия в соответствии с законами логики.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Swords14.jpg/349px-Swords14.jpg?20240406052249"),

    ("Туз пентаклей",
     "Карта указывает на новые начинания. Сейчас вы находитесь в переходном состоянии. Впереди вас ждет совершенно иная жизнь, полная удовольствий и возможностей. Вероятно, вы поменяете работу или пересмотрите свои приоритеты. Вы сможете достичь безопасности и стабильности. Однако будьте готовы потратить свое время и энергию.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Pents01.jpg/346px-Pents01.jpg?20240406052416"),
    ("Двойка пентаклей",
     "Это карта олицетворяет баланс, который очень легко разрушить. Вероятно, вы пытаетесь гармонично расставить приоритеты, стараясь удержать равновесие между всеми сферами жизни. Из-за многозадачности можно допустить ряд ошибок, постарайтесь сконцентрироваться на нескольких вещах. Вы также легко адаптируетесь к новым условиям, связанным с изменениями.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Pents02.jpg/347px-Pents02.jpg?20240406052450"),
    ("Тройка пентаклей",
     "Вы прекрасно работаете в команде и ладите со своими коллегами. Вероятно, скоро вам придется объединить усилия, чтобы справиться с крупным проектом. Карта сигнализирует о том, что благодаря разным навыкам вы способны добиться любых поставленных целей, только не сдавайтесь. Она также напоминает, что необходимо ценить опыт и таланты окружающих. Сотрудничая с ними, вы сможете достичь большего, чем в одиночку.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Pents03.jpg/349px-Pents03.jpg?20240406052515"),
    ("Четверка пентаклей",
     "У этой карты есть как положительные, так и отрицательные качества. С одной стороны, вы, вероятно, добились многих поставленных целей и достигли материального благополучия. С другой стороны, вы обращаете внимание только на финансовую составляющую. Это может превратить вас в жадного человека.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Pents04.jpg/346px-Pents04.jpg?20240406052537"),
    ("Пятерка пентаклей",
     "Карта предупреждает, что скоро ваше положение может ухудшиться. Скорее всего, вы столкнетесь с утратой, болезнью и чувством одиночества. Не исключено, что вы лишитесь достатка. Будьте готовы преодолевать все препятствия. Помните, что после дождя всегда появляется радуга.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Pents05.jpg/347px-Pents05.jpg?20240406052622"),
    ("Шестерка пентаклей",
     "Ваши доходы и расходы сбалансированы, поэтому вам не приходится беспокоиться за свое финансовое положение. Вы в состоянии позволить себе все, что хотите. Вы также благодарны за то, что имеете, поэтому занимаетесь благотворительностью, бескорыстно помогая нуждающимся.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Pents06.jpg/346px-Pents06.jpg?20240406052648"),
    ("Семерка пентаклей",
     "Вы, вероятно, думаете не только о настоящем, но и о будущем, поэтому много работаете и инвестируете средства. Все ваши усилия обязательно окупятся. Карта Таро Семерка Пентаклей также говорит о том, что вы боитесь неудач. Вас одолевают сомнения. Будьте смелее. Даже если ваши надежды не оправдаются, вы получите новый опыт и сможете извлечь уроки из своих ошибок.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Pents07.jpg/348px-Pents07.jpg?20240406052729"),
    ("Восьмерка пентаклей",
     "Вам необходимо сосредоточиться на своих задачах, они не обязательно должны быть связаны с карьерой. Усердно работайте для достижения своих целей. Не исключено, что дел будет много. В таком случае не бойтесь попросить помощи у окружающих. Они обязательно откликнутся на вашу просьбу. Сотрудничая с другими, вы сможете найти баланс между разными сферами жизни.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Pents08.jpg/349px-Pents08.jpg?20240406052800"),
    ("Девятка пентаклей",
     "Карта указывает на человека, который наконец-то стал независимым и самодостаточным. Ему пришлось пройти непростой путь, чтобы в конце концов обрести желаемое. Все трудности остались позади. Пришло время пожинать плоды своего упорного труда.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Pents09.jpg/346px-Pents09.jpg?20240406052838"),
    ("Десятка пентаклей",
     "Эта карта символизирует стабильность и удовлетворение. Она говорит о том, что все ваши усилия окупятся в будущем. Даже если вы сталкиваетесь с трудностями, помните, что всегда есть свет в конце туннеля. На вашем пути будет много препятствий, но вы все преодолеете. Не забывайте дарить радость близким людям, поверьте, глядя на их улыбки, вы почувствуете настоящее счастье.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Pents10.jpg/348px-Pents10.jpg?20240406052914"),
    ("Паж пентаклей",
     "Паж амбициозен и трудолюбив. Он сосредоточен на построении планов на будущее и достижении своих целей. Идеи этого человека довольно приземленные и реалистичные. Он также ценит природу и все ее дары. Карта указывает на то, что вам необходимо завершить начатое. У вас достаточно сил и энергии, чтобы справиться со сложными или скучными задачами. Ваш труд будет вознагражден.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Pents11.jpg/347px-Pents11.jpg?20240406052951"),
    ("Рыцарь пентаклей",
     "Вы полностью поглощены своими задачами, для вас важно, чтобы вы выполняли работу эффективно. У вас много терпения, вы готовы на все, чтобы успешно закончить все взятые на себя проекты. Окружающие восхищаются вашей преданностью своему делу и чувством долга. Но постарайтесь не превратиться в перфекциониста, это может усложнить вашу жизнь.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Pents12.jpg/347px-Pents12.jpg?20240406053020"),
    ("Королева пентаклей",
     "Эта королева успевает абсолютно все — она прекрасная домохозяйка, жена и мама, а также успешная карьеристка. Карта указывает на практичного, самодостаточного и осторожного человека. Он никогда не будет открыто обсуждать свое финансовое положение и делиться тайнами, но всегда протянет руку помощи нуждающемуся. Такая личность может быть в вашем окружении.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Pents13.jpg/346px-Pents13.jpg?20240406053044"),
    ("Король пентаклей",
     "Карта Таро Король Пентаклей указывает на ответственного и надежного человека, который заботится об окружающих. Ему не свойственна лень, он все время трудится и двигается к своим целям. Это может быть ваш более авторитетный и мудрый коллега. В таком случае он поможет вам подняться по карьерной лестнице, но будьте готовы к критике. Король Пентаклей предрекает успех. Правда, чтобы его достичь, необходимо работать не покладая рук.",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Pents14.jpg/345px-Pents14.jpg?20240406053113")
]

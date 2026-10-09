# Генератор страниц услуг «Чисто Алексей».
# Запуск: python3 tools/build_pages.py  (из корня репозитория)
# Правьте тексты в SERVICES ниже и перезапускайте, страницы пересоберутся.
import html, json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://chisto-alexey.ru"
PHONE = "+7 999 966-22-11"
TG = "https://t.me/Chisto_Alexey"
METRIKA = open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'metrika.html'), encoding='utf-8').read()

def back(href):
    return ('<a class="back-btn" href="' + href + '" onclick="if(document.referrer.indexOf(location.host)>-1&amp;&amp;history.length>1){history.back();return false;}">'
            '<span aria-hidden="true">←</span> Назад</a>')

PHONE_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
ZAYAVKA = "https://t.me/m/kkPA_OlCYzhi"  # ссылка «Оставить заявку» (Telegram с готовым текстом)

idx = (ROOT / "index.html").read_text(encoding="utf-8")
FAVICON = '<link rel="icon" href="/favicon.ico" sizes="any">\n<link rel="icon" type="image/png" sizes="120x120" href="/favicon-120.png">\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">'

SERVICES = [
 dict(slug="himchistka-divanov", menu="Химчистка диванов",
  title="Химчистка диванов на дому в Москве и Одинцово, от 5 000 ₽ | Чисто Алексей",
  desc="Химчистка дивана на дому: прямые, угловые, диваны-кровати. Экстракторная чистка обивки без вывоза мебели. Цена от 5 000 ₽. Москва, Одинцово и Московская область.",
  h1="Химчистка диванов на дому",
  lede="Профессиональная химчистка дивана на дому в Москве, Одинцово и Московской области. Алексей приезжает со своим экстрактором и чистит обивку прямо у вас дома, без вывоза мебели и без резкого запаха химии.",
  img="images/ba-12.jpg", img_alt="Химчистка углового дивана до и после",
  prices=[("Двухместный диван","от 5 000 ₽"),("Трёхместный диван","от 6 000 ₽"),("Угловой диван (4 места)","от 7 000 ₽"),("Выведение сложных пятен","от 500 ₽"),("Антибактериальная обработка","+1 000 ₽"),("Обивка из флока","+100% к стоимости")],
  text=[("Какие диваны чистим",[
    "Чистим прямые и угловые диваны, диваны-кровати, модульные диваны и диваны с отдельными подушками. Работаем с велюром, рогожкой, микрофиброй, шенилом, букле и другими тканями, состав подбирается под тип обивки.",
    "Химчистка дивана на дому убирает пятна от кофе, чая, вина, еды, следы от рук на подлокотниках, «засаленность» сидений и неприятный запах. Если пятно сложное (кровь, чернила, слайм, жир), Алексей выводит его отдельно."]),
   ("Почему экстракторная чистка",[
    "Экстрактор подаёт моющий раствор в ткань и сразу вытягивает его вместе с грязью. Поэтому чистка проходит глубоко, а не только по поверхности, и в обивке не остаётся лишней воды и моющего средства."])],
  photos=[("images/ba-12.jpg","Угловой диван: химчистка на дому"),("images/ba-3.jpg","Диван до и после химчистки"),("images/ba-4.jpg","Светлый диван: выведение пятен"),("images/ba-11.jpg","Диван с пуфом до и после химчистки")],
  faq=[("Сколько стоит химчистка дивана?","Базовая цена: от 5 000 ₽ за двухместный, от 6 000 ₽ за трёхместный и от 7 000 ₽ за угловой диван. Точную стоимость Алексей называет на месте, после осмотра степени загрязнения."),
       ("Сколько сохнет диван после химчистки?","Зависит от ткани, влажности и погоды, обычно от нескольких часов до суток. Ускорить высыхание можно с помощью сушки (2 500 ₽/час)."),
       ("Нужно ли снимать чехлы или подушки?","Нет. Алексей чистит диван целиком на месте: сиденья, спинку, подлокотники и съёмные подушки."),
       ("Уйдут ли все пятна?","Большинство бытовых пятен уходит полностью. Застарелые и сложные пятна выводятся отдельно, Алексей честно скажет на осмотре, какой результат реально получить.")]),
 dict(slug="himchistka-matrasov", menu="Химчистка матрасов",
  title="Химчистка матрасов на дому в Москве и Одинцово, от 3 000 ₽ | Чисто Алексей",
  desc="Химчистка матраса на дому: пятна, запах, пыль. Экстракторная чистка, антибактериальная обработка. От 3 000 ₽ за сторону. Москва, Одинцово, Московская область.",
  h1="Химчистка матрасов на дому",
  lede="Чистка матраса на дому в Москве и Одинцово: убираем пятна, разводы и неприятный запах. Экстракторная химчистка без вывоза матраса: вы ложитесь спать на чистое уже в день чистки или на следующий.",
  img="images/work-mattress.jpg", img_alt="Алексей чистит матрас экстрактором",
  prices=[("Матрас, одна сторона","от 3 000 ₽"),("Антибактериальная обработка","+1 000 ₽"),("Нейтрализация запахов","от 1 500 ₽"),("Выведение сложных пятен","от 500 ₽"),("Сушка","2 500 ₽/час")],
  text=[("Когда нужна химчистка матраса",[
    "Матрас незаметно накапливает пот, пыль, пятна от напитков и следы домашних животных. Обычная влажная уборка их не достаёт: нужна глубокая чистка, которая вытягивает грязь из наполнителя.",
    "Делаем химчистку матрасов любых размеров: односпальных, полуторных, двуспальных, детских. Можно чистить одну или обе стороны."]),
   ("Запах и пятна",[
    "Для сложных случаев есть нейтрализация запахов и антибактериальная обработка, их добавляют к основной чистке. Средства безопасны для людей и домашних животных."])],
  photos=[("images/work-mattress.jpg","Химчистка матраса на дому"),("images/hero-mattress.jpg","Обработка матраса перед химчисткой")],
  faq=[("Сколько стоит химчистка матраса?","От 3 000 ₽ за одну сторону. Итог зависит от размера матраса и степени загрязнения, точную цену Алексей называет на месте."),
       ("Когда можно спать на матрасе?","Обычно матрас высыхает от нескольких часов до суток. Чтобы ускорить, можно заказать сушку."),
       ("Убирается ли запах?","Да, для этого есть отдельная услуга: нейтрализация запахов (от 1 500 ₽). Она работает с причиной запаха, а не маскирует его.")]),
 dict(slug="himchistka-kresel-i-stulev", menu="Химчистка кресел и стульев",
  title="Химчистка кресел и стульев на дому: кресло от 3 000 ₽, стул от 1 000 ₽ | Чисто Алексей",
  desc="Химчистка кресел, стульев и офисных кресел на дому и в офисе. Экстракторная чистка обивки. Кресло от 3 000 ₽, стул от 1 000 ₽. Москва, Одинцово.",
  h1="Химчистка кресел и стульев",
  lede="Чистим кресла, обеденные стулья с мягкой обивкой и офисные кресла: дома, в офисе, в кафе. Экстракторная химчистка на месте, без вывоза мебели.",
  img="images/work-armchair.jpg", img_alt="Алексей чистит кресло из букле",
  prices=[("Кресло","от 3 000 ₽"),("Стул","от 1 000 ₽"),("Офисный стул / кресло","от 2 000 ₽"),("Выведение сложных пятен","от 500 ₽"),("Обивка из флока","+100% к стоимости")],
  text=[("Что чистим",[
    "Кресла и кресла-реклайнеры, обеденные стулья с тканевой обивкой, барные стулья, офисные кресла и стулья для переговорных. Работаем с велюром, букле, рогожкой и другими тканями.",
    "Для офисов и кафе чистим стулья партиями, так удобно заказать сразу весь зал."])],
  photos=[("images/ba-5.jpg","Стул до и после химчистки"),("images/ba-6.jpg","Кресло-стул до и после химчистки"),("images/work-armchair.jpg","Химчистка кресла на дому")],
  faq=[("Сколько стоит химчистка стула?","От 1 000 ₽ за обычный стул и от 2 000 ₽ за офисный. Кресло от 3 000 ₽."),
       ("Есть ли скидка на много стульев?","Стоимость партии обсуждается индивидуально, напишите Алексею количество и фото стульев."),
       ("Можно ли почистить стулья в офисе?","Да, работаем с юридическими лицами: наличный и безналичный расчёт, без НДС.")]),
 dict(slug="himchistka-kovrov", menu="Химчистка ковров и ковролина",
  title="Химчистка ковров и ковролина на дому и в офисе, от 300 ₽/м² | Чисто Алексей",
  desc="Химчистка ковров и ковролина на месте: дома и в офисе. Экстракторная чистка, выведение пятен. От 300 ₽ за м². Москва, Одинцово, Московская область.",
  h1="Химчистка ковров и ковролина",
  lede="Чистим ковры и ковролин на месте: дома и в офисе, без вывоза в цех. Экстракторная химчистка вытягивает грязь из ворса и освежает цвет.",
  img="images/ba-7.jpg", img_alt="Ковролин до и после химчистки",
  prices=[("Ковры и ковролин","от 300 ₽/м²"),("Выведение сложных пятен","от 500 ₽"),("Нейтрализация запахов","от 1 500 ₽"),("Сушка","2 500 ₽/час")],
  text=[("Ковры и ковролин без вывоза",[
    "Чистка ковров на дому избавляет от пятен, пыли в ворсе и тусклого цвета. Ковёр не нужно скатывать и везти в химчистку: Алексей всё делает на месте.",
    "Ковролин в офисах, переговорных и коридорах чистим целиком. Можно договориться о чистке в нерабочее время."])],
  photos=[("images/ba-7.jpg","Ковролин до и после химчистки")],
  faq=[("Сколько стоит химчистка ковра?","От 300 ₽ за квадратный метр. Цена зависит от площади, длины ворса и степени загрязнения."),
       ("Чистите ковролин в офисе?","Да. Работаем с юрлицами, наличный и безналичный расчёт, без НДС.")]),
 dict(slug="himchistka-shtor", menu="Химчистка штор без снятия",
  title="Химчистка штор без снятия на дому, от 500 ₽/м² | Чисто Алексей",
  desc="Химчистка штор на дому без снятия с карниза. Экстракторная чистка портьер и плотных штор. От 500 ₽ за м². Москва, Одинцово, Московская область.",
  h1="Химчистка штор без снятия",
  lede="Чистим шторы и портьеры прямо на карнизе: снимать, стирать и гладить не нужно. Подходит для плотных и тяжёлых штор, которые неудобно снимать и везти в химчистку.",
  img="images/work-curtains.jpg", img_alt="Алексей чистит шторы без снятия",
  prices=[("Шторы без снятия, одна сторона","от 500 ₽/м²"),("Выведение сложных пятен","от 500 ₽"),("Нейтрализация запахов","от 1 500 ₽")],
  text=[("Как это работает",[
    "Экстрактор с насадкой для вертикальных поверхностей проходит ткань сверху вниз, подавая раствор и сразу забирая его вместе с пылью и грязью. Шторы остаются на месте и не теряют форму.",
    "Химчистка штор без снятия особенно удобна для высоких окон, панорамного остекления и тяжёлых портьер."])],
  photos=[("images/work-curtains.jpg","Химчистка штор на дому"),("images/ba-curtain.jpg","Химчистка штор без снятия с карниза")],
  faq=[("Сколько стоит химчистка штор?","От 500 ₽ за квадратный метр (одна сторона). Итог зависит от площади и ткани."),
       ("Нужно ли снимать шторы?","Нет, в этом и смысл. Шторы чистятся прямо на карнизе.")]),
 dict(slug="himchistka-dlya-biznesa", menu="Для бизнеса: офисы и рестораны",
  title="Химчистка мебели и ковролина для офисов, ресторанов и кафе | Чисто Алексей",
  desc="Химчистка для бизнеса: ковролин в офисах, диваны, кресла и стулья в ресторанах и кафе. Работаем с юрлицами, наличный и безналичный расчёт без НДС. Москва, Одинцово.",
  h1="Химчистка для офисов, ресторанов и кафе",
  lede="Чистим ковролин в офисах, диваны, банкетки, кресла и стулья в ресторанах и кафе. Работаем с юридическими лицами: наличный и безналичный расчёт, без НДС.",
  img="images/ba-7.jpg", img_alt="Чистка ковролина в офисе",
  prices=[("Ковролин","от 300 ₽/м²"),("Диваны и банкетки","от 5 000 ₽"),("Кресло","от 3 000 ₽"),("Стул","от 1 000 ₽"),("Офисный стул / кресло","от 2 000 ₽")],
  text=[("Для кого",[
    "Офисы и коворкинги: ковролин, кресла, диваны в зонах отдыха и переговорных. Рестораны, кафе и бары: диваны, банкетки, мягкие стулья в зале. Салоны, клиники, гостиницы: мягкая мебель в зонах ожидания.",
    "Стоимость для большого объёма, например всего зала или этажа, обсуждается индивидуально."]),
   ("Документы и оплата",[
    "Наличный и безналичный расчёт, без НДС. Напишите Алексею, что нужно почистить и сколько, и он назовёт цену и согласует удобное время."])],
  photos=[("images/ba-7.jpg","Химчистка ковролина"),("images/ba-5.jpg","Химчистка стульев"),("images/work-armchair.jpg","Химчистка кресел")],
  faq=[("Работаете с юрлицами?","Да: наличный и безналичный расчёт, без НДС."),
       ("Можно ли в нерабочее время?","Время согласуется с Алексеем, напишите удобные даты и часы.")]),
]

def esc(s): return html.escape(s, quote=True)

NAV = '''    <button class="burger" type="button" aria-label="Меню" onclick="document.body.classList.toggle('menu-open')"><span></span><span></span><span></span></button>
    <nav>
      <a href="ceny.html">Услуги и цены</a>
      <a href="raboty.html">Работы</a>
      <a href="himchistka-dlya-biznesa.html">Для бизнеса</a>
      <a href="otzyvy.html">Отзывы</a>
      <a href="news.html">Новости</a>
      <a href="kontakty.html">Контакты</a>
      <a class="nav-call" href="tel:+79999662211">Позвонить: +7 999 966-22-11</a>
    </nav>'''

def foot_links():
    return '\n'.join(f'      <a href="{s["slug"]}.html">{esc(s["menu"])}</a>' for s in SERVICES)

INN = "422378559089"
OGRNIP = "321420500065049"
OKPO = "2009482280"
EMAIL = "himchistka@chisto-alexey.ru"

FOOTER = f'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-col foot-about">
        <a class="foot-logo" href="index.html"><img src="images/logo.png" alt="Чисто Алексей"></a>
        <p>Химчистка мягкой мебели, ковров и штор на дому и в офисе. Москва, Одинцово и Московская область.</p>
        <a class="btn btn-primary foot-btn" href="{ZAYAVKA}" target="_blank" rel="noopener">Узнать цену по фото</a>
      </div>
      <div class="foot-col">
        <h3>Услуги</h3>
{foot_links()}
      </div>
      <div class="foot-col">
        <h3>Разделы</h3>
        <a href="ceny.html">Услуги и цены</a>
        <a href="raboty.html">Работы до и после</a>
        <a href="otzyvy.html">Отзывы</a>
        <a href="news.html">Новости</a>
        <a href="kontakty.html">Контакты</a>
      </div>
      <div class="foot-col foot-contacts">
        <h3>Контакты</h3>
        <a class="foot-phone" href="tel:+79999662211">{PHONE}</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="https://t.me/Chisto_Aleksey" target="_blank" rel="noopener">Telegram-канал</a>
        <span>Москва, Ярославская ул., 8, корп. 3</span>
        <span>Одинцово, ул. Ракетчиков, с11</span>
      </div>
    </div>
    <div class="foot-seo">
      <h3>Популярные услуги</h3>
      <div class="foot-tags">
        <a href="himchistka-divanov.html">Химчистка дивана на дому</a>
        <a href="himchistka-divanov.html">Химчистка углового дивана</a>
        <a href="himchistka-divanov.html">Химчистка прямого дивана</a>
        <a href="himchistka-divanov.html">Химчистка дивана-кровати</a>
        <a href="himchistka-divanov.html">Химчистка светлого дивана</a>
        <a href="himchistka-divanov.html">Чистка дивана от пятен</a>
        <a href="himchistka-divanov.html">Удаление запаха с дивана</a>
        <a href="himchistka-divanov.html">Химчистка дивана из велюра</a>
        <a href="himchistka-divanov.html">Химчистка дивана из рогожки</a>
        <a href="himchistka-divanov.html">Химчистка дивана из букле</a>
        <a href="himchistka-divanov.html">Химчистка кожаного дивана</a>
        <a href="himchistka-matrasov.html">Химчистка матраса на дому</a>
        <a href="himchistka-matrasov.html">Чистка матраса от пятен</a>
        <a href="himchistka-matrasov.html">Химчистка детского матраса</a>
        <a href="himchistka-matrasov.html">Удаление запаха с матраса</a>
        <a href="himchistka-matrasov.html">Чистка ортопедического матраса</a>
        <a href="himchistka-kresel-i-stulev.html">Химчистка кресла</a>
        <a href="himchistka-kresel-i-stulev.html">Химчистка стульев</a>
        <a href="himchistka-kresel-i-stulev.html">Химчистка офисных кресел</a>
        <a href="himchistka-kresel-i-stulev.html">Химчистка обеденных стульев</a>
        <a href="himchistka-kresel-i-stulev.html">Чистка компьютерного кресла</a>
        <a href="himchistka-kresel-i-stulev.html">Химчистка пуфа и банкетки</a>
        <a href="himchistka-kovrov.html">Химчистка ковров на дому</a>
        <a href="himchistka-kovrov.html">Чистка ковролина</a>
        <a href="himchistka-kovrov.html">Химчистка ковролина в офисе</a>
        <a href="himchistka-kovrov.html">Чистка ковра от пятен</a>
        <a href="himchistka-shtor.html">Химчистка штор без снятия</a>
        <a href="himchistka-shtor.html">Чистка штор на дому</a>
        <a href="himchistka-shtor.html">Чистка портьер и тюля</a>
        <a href="himchistka-shtor.html">Химчистка римских штор</a>
        <a href="himchistka-dlya-biznesa.html">Химчистка мебели в офисе</a>
        <a href="himchistka-dlya-biznesa.html">Химчистка мебели в ресторане</a>
        <a href="himchistka-dlya-biznesa.html">Химчистка мебели в кафе</a>
        <a href="himchistka-dlya-biznesa.html">Химчистка для юрлиц</a>
        <a href="himchistka-dlya-biznesa.html">Чистка мебели в гостинице</a>
        <a href="ceny.html">Цены на химчистку мебели</a>
        <a href="ceny.html">Выведение сложных пятен</a>
        <a href="ceny.html">Антибактериальная обработка мебели</a>
        <a href="ceny.html">Нейтрализация запахов</a>
        <a href="ceny.html">Гидрофобная защита мебели</a>
        <a href="ceny.html">Химчистка мебели недорого</a>
        <a href="kontakty.html">Химчистка мебели в Москве</a>
        <a href="kontakty.html">Химчистка мебели в Одинцово</a>
        <a href="kontakty.html">Химчистка мебели в Московской области</a>
        <a href="kontakty.html">Выездная химчистка мебели</a>
        <a href="kontakty.html">Химчистка мебели у ВДНХ</a>
      </div>
    </div>
    <div class="foot-legal">
      <span>© 2026 «Чисто Алексей» · ИП Гарифуллина Лилия Харисовна · ИНН {INN} · ОГРНИП {OGRNIP}</span>
      <span><a href="rekvizity.html">Реквизиты</a> · <a href="privacy.html">Политика конфиденциальности</a></span>
    </div>
  </div>
</footer>'''

def page(s):
    url = f'{SITE}/{s["slug"]}.html'
    prices = '\n'.join(f'          <div class="price-row"><div class="price-meta"><span class="price-name">{esc(n)}</span></div><span class="price-num">{esc(v)}</span></div>' for n, v in s["prices"])
    text = '\n'.join(f'      <h2>{esc(h)}</h2>\n' + '\n'.join(f'      <p>{esc(p)}</p>' for p in ps) for h, ps in s["text"])
    photos = '\n'.join(f'        <figure><div class="frame"><img src="{src}" alt="{esc(a)}" loading="lazy"></div><figcaption>{esc(a)}</figcaption></figure>' for src, a in s["photos"])
    faq = '\n'.join(f'        <details{" open" if i == 0 else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for i, (q, a) in enumerate(s["faq"]))
    others = '\n'.join(f'        <a href="{o["slug"]}.html">{esc(o["menu"])}</a>' for o in SERVICES if o is not s)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": s["h1"], "serviceType": s["menu"], "description": s["desc"], "url": url,
         "areaServed": ["Москва", "Одинцово", "Московская область"],
         "provider": {"@type": "LocalBusiness", "name": "Чисто Алексей", "telephone": "+79999662211", "email": "himchistka@chisto-alexey.ru", "url": SITE + "/"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Главная", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": s["menu"], "item": url}]}]}
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(s["title"])}</title>
<meta name="description" content="{esc(s["desc"])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{esc(s["title"])}">
<meta property="og:description" content="{esc(s["desc"])}">
<meta property="og:image" content="{SITE}/{s["img"]}">
<meta property="og:url" content="{url}">
{FAVICON}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css?v=1009h">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{METRIKA}</head>
<body>
<header>
  <div class="wrap headrow">
    <a class="brand" href="index.html"><span class="brand-logo-wrap"><img src="images/logo.png" alt="Чисто Алексей"></span></a>
{NAV}
    <div class="head-cta">
      <a class="head-phone" href="tel:+79999662211" aria-label="Позвонить Алексею">{PHONE_SVG}<span>+7 999 966-22-11</span></a>
      <a class="btn btn-primary" href="{ZAYAVKA}" target="_blank" rel="noopener">Оставить заявку</a>
    </div>
  </div>
</header>

<main>
  <div class="wrap crumbs-row">{back("ceny.html#svc-more")}<p class="crumbs"><a href="index.html">Главная</a> / {esc(s["menu"])}</p></div>
  <section>
    <div class="wrap svc-hero">
      <div>
        <span class="eyebrow">Москва · Одинцово · Московская область</span>
        <h1>{esc(s["h1"])}</h1>
        <p class="lede">{esc(s["lede"])}</p>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="{ZAYAVKA}" target="_blank" rel="noopener">Узнать цену по фото</a>
          <a class="btn btn-ghost" href="tel:+79999662211">{PHONE}</a>
        </div>
      </div>
      <div class="svc-hero-img"><img src="{s["img"]}" alt="{esc(s["img_alt"])}"></div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head"><h2>Цены</h2><p class="section-note">Базовая стоимость. Точная цена после осмотра, до начала работ.</p></div>
      <div class="price-group">
{prices}
      </div>
      <p class="price-note"><a href="ceny.html" style="color:inherit">Весь прайс</a> · Наличный и безналичный расчёт</p>
    </div>
  </section>

  <section>
    <div class="wrap"><div class="svc-text">
{text}
    </div></div>
  </section>

  <section>
    <div class="wrap svc-sec">
      <h2>Как проходит химчистка</h2>
      <div class="svc-steps">
        <div><b>Заявка</b><span>Пишете в Telegram или звоните, присылаете фото.</span></div>
        <div><b>Осмотр и цена</b><span>Алексей оценивает загрязнение и называет точную стоимость.</span></div>
        <div><b>Чистка на месте</b><span>Экстракторная химчистка без вывоза мебели.</span></div>
        <div><b>Результат</b><span>Сразу видите разницу, при необходимости фото до/после.</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head"><h2>Работы Алексея</h2></div>
      <div class="gallery">
{photos}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head"><h2>Частые вопросы</h2></div>
      <div class="faq">
{faq}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap svc-cta">
      <div><h2>Узнайте точную цену</h2><p>Пришлите фото в Telegram, и Алексей ответит и предложит время выезда.</p></div>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="{ZAYAVKA}" target="_blank" rel="noopener">Оставить заявку</a>
        <a class="btn btn-ghost" href="tel:+79999662211">Позвонить</a>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2 style="font-size:1.3rem;margin:0;">Другие услуги</h2>
      <div class="svc-links">
{others}
      </div>
    </div>
  </section>
</main>

{FOOTER}
</body>
</html>
'''

for s in SERVICES:
    (ROOT / f'{s["slug"]}.html').write_text(page(s), encoding="utf-8")


def simple_page(slug, title, desc, h1, body):
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}/{slug}.html">
{FAVICON}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css?v=1009h">
{METRIKA}</head>
<body>
<header>
  <div class="wrap headrow">
    <a class="brand" href="index.html"><span class="brand-logo-wrap"><img src="images/logo.png" alt="Чисто Алексей"></span></a>
{NAV}
    <div class="head-cta">
      <a class="head-phone" href="tel:+79999662211" aria-label="Позвонить Алексею">{PHONE_SVG}<span>+7 999 966-22-11</span></a>
      <a class="btn btn-primary" href="{ZAYAVKA}" target="_blank" rel="noopener">Оставить заявку</a>
    </div>
  </div>
</header>
<main>
  <div class="wrap crumbs-row">{back("index.html")}<p class="crumbs"><a href="index.html">Главная</a> / {esc(h1)}</p></div>
  <section>
    <div class="wrap"><div class="svc-text legal-text">
      <h1 style="font-size:clamp(1.6rem,3vw,2.2rem);margin:0 0 20px;">{esc(h1)}</h1>
{body}
    </div></div>
  </section>
</main>

{FOOTER}
</body>
</html>
'''

REKV = f'''      <table class="rekv">
        <tr><th>Исполнитель</th><td>Индивидуальный предприниматель Гарифуллина Лилия Харисовна (ИП Гарифуллина Л.Х.)</td></tr>
        <tr><th>Бренд</th><td>«Чисто Алексей», химчистка мебели на дому</td></tr>
        <tr><th>ИНН</th><td>{INN}</td></tr>
        <tr><th>ОГРНИП</th><td>{OGRNIP}</td></tr>
        <tr><th>ОКПО</th><td>{OKPO}</td></tr>
        <tr><th>Адреса работы</th><td>Москва, Ярославская ул., 8, корп. 3<br>Одинцово, ул. Ракетчиков, с11</td></tr>
        <tr><th>Телефон</th><td><a href="tel:+79999662211">{PHONE}</a></td></tr>
        <tr><th>Эл. почта</th><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr>
      </table>
      <p>Банковские реквизиты для оплаты по безналичному расчёту (для юридических лиц) направляем по запросу на <a href="mailto:{EMAIL}">{EMAIL}</a> или в Telegram вместе со счётом.</p>
'''

PRIV = [
 ("1. Общие положения", [
  f"Настоящая политика определяет порядок обработки и защиты персональных данных посетителей сайта chisto-alexey.ru (далее: Сайт) в соответствии с Федеральным законом от 27.07.2006 № 152-ФЗ «О персональных данных».",
  f"Оператор персональных данных: индивидуальный предприниматель Гарифуллина Лилия Харисовна, ИНН {INN}, ОГРНИП {OGRNIP} (далее: Оператор). Контакт для обращений: {EMAIL}.",
  "Используя Сайт и передавая Оператору свои данные, пользователь соглашается с настоящей политикой."]),
 ("2. Какие данные обрабатываются", [
  "Имя, номер телефона, имя пользователя в Telegram, адрес выезда мастера, фотографии мебели и описание загрязнений, если пользователь сам сообщает их при оформлении заявки по телефону, в Telegram или по электронной почте.",
  "Технические данные, которые браузер передаёт автоматически: IP-адрес, тип браузера и устройства, файлы cookie, сведения о посещённых страницах."]),
 ("3. Цели обработки", [
  "Обработка заявок, связь с клиентом, расчёт стоимости и согласование времени выезда.",
  "Оказание услуг химчистки, выставление счетов и выполнение договорных обязательств.",
  "Улучшение работы Сайта и анализ его посещаемости."]),
 ("4. Правовые основания", [
  "Согласие субъекта персональных данных, а также необходимость исполнения договора, стороной которого является субъект (п. 1 и 5 ч. 1 ст. 6 Закона № 152-ФЗ)."]),
 ("5. Порядок и сроки обработки", [
  "Оператор обрабатывает данные с использованием средств автоматизации и без них: сбор, запись, систематизация, хранение, уточнение, использование, удаление.",
  "Данные хранятся не дольше, чем этого требуют цели обработки, либо до отзыва согласия, если иное не предусмотрено законом.",
  "Оператор не передаёт персональные данные третьим лицам, за исключением случаев, предусмотренных законодательством РФ."]),
 ("6. Сторонние сервисы", [
  "На Сайте используются сторонние сервисы: виджет отзывов MyReviews (отзывы с Яндекс Карт), шрифты Google Fonts, переходы в Telegram. Эти сервисы могут получать технические данные браузера по своим правилам."]),
 ("7. Файлы cookie", [
  "Сайт и подключённые сервисы могут использовать cookie для корректной работы и статистики. Для анализа посещаемости используется сервис Яндекс.Метрика (ООО «Яндекс»), который обрабатывает обезличенные данные о визитах. Пользователь может отключить cookie в настройках браузера; часть функций Сайта при этом может работать некорректно."]),
 ("8. Защита данных", [
  "Оператор принимает необходимые правовые, организационные и технические меры для защиты персональных данных от неправомерного доступа, изменения, распространения и уничтожения."]),
 ("9. Права пользователя", [
  f"Пользователь вправе получить сведения об обработке своих данных, потребовать их уточнения, блокирования или удаления, а также отозвать согласие, направив запрос на {EMAIL}. Оператор отвечает в течение 10 рабочих дней."]),
 ("10. Изменение политики", [
  "Оператор может изменять настоящую политику. Новая редакция вступает в силу с момента размещения на Сайте. Редакция от 8 октября 2026 года."]),
]
PRIV_BODY = '\n'.join(f'      <h2>{esc(h)}</h2>\n' + '\n'.join(f'      <p>{esc(x)}</p>' for x in ps) for h, ps in PRIV)

(ROOT / "privacy.html").write_text(simple_page("privacy", "Политика конфиденциальности | Чисто Алексей",
    "Политика обработки персональных данных сайта chisto-alexey.ru, ИП Гарифуллина Л.Х.", "Политика конфиденциальности", PRIV_BODY), encoding="utf-8")
(ROOT / "rekvizity.html").write_text(simple_page("rekvizity", "Реквизиты | Чисто Алексей",
    "Реквизиты ИП Гарифуллина Л.Х., химчистка мебели «Чисто Алексей».", "Реквизиты", REKV), encoding="utf-8")


ART_BODY = """      <p><b>9 октября 2026 · Советы по уходу</b></p>
      <p>Если у вас кошка или собака, шерсть на ковре появляется быстрее, чем вы успеваете её убрать. Рассказываем, как справиться с ней дома, и когда пора звать химчистку.</p>
      <h2>1. Пылесос с турбощёткой</h2>
      <p>Ведите щётку медленно и в разных направлениях: сначала по ворсу, потом против. Так шерсть вытягивается из основания ковра, а не только с поверхности.</p>
      <h2>2. Липкий ролик или скотч</h2>
      <p>Подходит для небольших участков: у дивана, у лежанки питомца, на коротком ворсе.</p>
      <h2>3. Влажная резиновая перчатка</h2>
      <p>Проведите ладонью по ковру в одну сторону: шерсть собирается в комочки, которые легко убрать руками или пылесосом.</p>
      <h2>4. Резиновая щётка или скребок</h2>
      <p>Специальные щётки с резиновыми зубцами хорошо достают шерсть из ковролина и ковров с плотным ворсом.</p>
      <h2>5. Регулярная влажная чистка</h2>
      <p>Шерсть смешивается с пылью и жиром, и обычный пылесос перестаёт её вытягивать. Экстракторная химчистка вымывает её вместе с грязью и убирает запах животных.</p>
      <h2>Когда звать химчистку</h2>
      <p>Если ковёр потускнел, появился запах или следы питомца, пришлите фото Алексею: он назовёт стоимость до выезда. Химчистка ковров от 300 ₽ за м², удаление запаха мочи животных от 1 500 ₽.</p>
      <p><a class="btn btn-primary" href="https://t.me/m/kkPA_OlCYzhi" target="_blank" rel="noopener">Узнать цену по фото</a> &nbsp; <a href="himchistka-kovrov.html">Химчистка ковров и ковролина →</a></p>"""
(ROOT / "kak-ubrat-sherst-s-kovra.html").write_text(simple_page("kak-ubrat-sherst-s-kovra", "Как убрать шерсть с ковра: 5 способов | Чисто Алексей",
    "Как убрать шерсть кошки или собаки с ковра дома: 5 способов и когда нужна химчистка ковра. Советы мастера химчистки «Чисто Алексей».", "Как убрать шерсть с ковра: 5 способов", ART_BODY), encoding="utf-8")

# отдельные страницы разделов (контент берётся из tools/parts)
PARTS = ROOT / "tools" / "parts"
def part(name): return (PARTS / f"{name}.html").read_text(encoding="utf-8")
SVC_LINKS = '<div class="svc-links">\n' + '\n'.join(f'        <a href="{s["slug"]}.html">{esc(s["menu"])}</a>' for s in SERVICES) + '\n      </div>'

def section_page(slug, title, desc, crumb, body, extra=""):
    if '<h1' not in body:
        body = re.sub(r'<h2([^>]*)>', r'<h1 class="page-h1"\1>', body, count=1)
        body = body.replace('</h2>', '</h1>', 1)
    html_ = simple_page(slug, title, desc, crumb, "@@BODY@@")
    a = html_.index('  <section>\n    <div class="wrap"><div class="svc-text legal-text">')
    b = html_.index('</main>')
    html_ = html_[:a] + body + html_[b:]
    if extra: html_ = html_.replace('</body>', extra + '</body>')
    return html_

services_part = re.sub(r'\n *<h3 class="svc-links-h"[^>]*>.*?</div>', '', part("services"), flags=re.S)
services_part = services_part.replace('\n      <div class="price-perks">', '\n      <h3 class="svc-links-h" id="svc-more">Подробнее об услугах</h3>\n      ' + SVC_LINKS + '\n\n      <div class="price-perks">', 1)
SECTION_PAGES = [
  ("ceny", "Цены на химчистку мебели на дому в Москве и Одинцово | Чисто Алексей",
   "Прайс на химчистку диванов, матрасов, кресел, стульев, ковров и штор на дому. Что входит в чистку, когда бывают доплаты, ответы на вопросы.",
   "Услуги и цены", services_part + "\n" + part("faq"), ""),
  ("raboty", "Работы: фото до и после химчистки мебели | Чисто Алексей",
   "Фото до и после химчистки диванов, кресел, стульев и ковролина с реальных выездов Алексея. Как проходит химчистка на дому.",
   "Работы", part("results") + "\n" + part("process"), ""),
  ("otzyvy", "Отзывы о химчистке мебели «Чисто Алексей»",
   "Реальные отзывы клиентов с Яндекс.Карт о химчистке диванов, матрасов, ковролина и мебели в кафе.",
   "Отзывы", part("reviews"), part("reviews_script")),
  ("kontakty", "Контакты: химчистка мебели «Чисто Алексей», Москва и Одинцово",
   "Телефон, Telegram, почта и адреса химчистки мебели «Чисто Алексей» в Москве и Одинцово.",
   "Контакты", part("contacts").replace('<span class="eyebrow">Заявка на химчистку</span>', '<h1 class="eyebrow" style="font-size:.95rem;margin:0;">Контакты · Москва и Одинцово</h1>', 1).replace('<section id="contacts" style="padding-top:0;">', '<section id="contacts">', 1) + "\n" + part("charity"), ""),
]
for slug, title, desc, crumb, body, extra in SECTION_PAGES:
    (ROOT / f"{slug}.html").write_text(section_page(slug, title, desc, crumb, body, extra), encoding="utf-8")

# sitemap + robots
urls = [SITE + "/", SITE + "/ceny.html", SITE + "/raboty.html", SITE + "/otzyvy.html", SITE + "/kontakty.html", SITE + "/news.html", SITE + "/kak-ubrat-sherst-s-kovra.html", SITE + "/rekvizity.html", SITE + "/privacy.html"] + [f'{SITE}/{s["slug"]}.html' for s in SERVICES]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n', encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

# общий подвал и меню в index.html и news.html
for name in ("index.html", "news.html"):
    p = ROOT / name; t = p.read_text(encoding="utf-8")
    t = re.sub(r'<footer>.*?</footer>', FOOTER, t, flags=re.S)
    t = re.sub(r'(    <button class="burger"[^\n]*\n)?    <nav>.*?</nav>', lambda m: NAV, t, count=1, flags=re.S)
    p.write_text(t, encoding="utf-8")

# подсветка текущего раздела в меню
for f in ROOT.glob("*.html"):
    t = f.read_text(encoding="utf-8")
    t = t.replace(' aria-current="page"', '')
    if '    <nav>' in t:
        a = t.index('    <nav>'); b = t.index('</nav>', a)
        t = t[:a] + t[a:b].replace(f'<a href="{f.name}">', f'<a href="{f.name}" aria-current="page">', 1) + t[b:]
    f.write_text(t, encoding="utf-8")
print("ok", len(SERVICES), "pages")

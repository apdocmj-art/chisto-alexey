/* «Заказать звонок»: окно с формой, заявка уходит на почту через FormSubmit */
(function(){
  var TO='himchistka@chisto-alexey.ru';
  var css=''+
  '.cb-modal{position:fixed;inset:0;z-index:1100;background:rgba(5,15,25,.6);display:flex;align-items:center;justify-content:center;padding:16px;opacity:0;visibility:hidden;transition:.2s}'+
  '.cb-modal.open{opacity:1;visibility:visible}'+
  '.cb-box{position:relative;width:100%;max-width:400px;background:#fff;color:#0F2533;border-radius:20px;padding:26px 22px 22px;box-shadow:0 20px 60px rgba(0,0,0,.35);transform:translateY(12px);transition:.2s;font-family:inherit}'+
  '.cb-modal.open .cb-box{transform:none}'+
  '.cb-x{position:absolute;top:12px;right:12px;border:0;background:#EEF3F5;width:34px;height:34px;border-radius:50%;font-size:1.3rem;line-height:1;cursor:pointer;color:#0F2533}'+
  '.cb-box h3{margin:0 0 6px;font-size:1.35rem;line-height:1.2}'+
  '.cb-box p.cb-sub{margin:0 0 16px;color:#5B6B75;font-size:.92rem}'+
  '.cb-box label{display:block;font-size:.82rem;font-weight:700;margin:10px 0 5px;color:#33505F}'+
  '.cb-box input[type=text],.cb-box input[type=tel],.cb-box textarea{width:100%;box-sizing:border-box;border:1.5px solid #D5E1E6;border-radius:12px;padding:12px 14px;font:inherit;font-size:1rem;color:#0F2533;background:#F7FAFB;outline:none}'+
  '.cb-box textarea{min-height:64px;resize:vertical}'+
  '.cb-box input:focus,.cb-box textarea:focus{border-color:#2FD0CA;background:#fff}'+
  '.cb-agree{display:flex;gap:8px;align-items:flex-start;font-size:.78rem;color:#5B6B75;margin:12px 0 4px;font-weight:400!important}'+
  '.cb-agree a{color:#0F9C97}'+
  '.cb-send{width:100%;margin-top:12px;border:0;border-radius:14px;padding:15px;font:inherit;font-weight:800;font-size:1rem;background:#2FD0CA;color:#062A2A;cursor:pointer}'+
  '.cb-send:disabled{opacity:.6;cursor:wait}'+
  '.cb-err{color:#C0392B;font-size:.85rem;margin-top:8px;min-height:1em}'+
  '.cb-ok{text-align:center;padding:10px 0}'+
  '.cb-ok .cb-ic{font-size:2.6rem}'+
  '.cb-hp{position:absolute;left:-9999px;opacity:0}'+
  '.cb-btn{cursor:pointer}';
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);

  var m=document.createElement('div');m.className='cb-modal';m.setAttribute('role','dialog');m.setAttribute('aria-label','Заказать звонок');
  m.innerHTML='<div class="cb-box"><button type="button" class="cb-x" aria-label="Закрыть">×</button>'+
   '<div class="cb-form-wrap"><h3>Заказать звонок</h3><p class="cb-sub">Оставьте номер, и Алексей перезвонит вам в ближайшее время.</p>'+
   '<form novalidate>'+
   '<label for="cb-name">Ваше имя</label><input id="cb-name" type="text" name="name" autocomplete="name" placeholder="Например, Анна">'+
   '<label for="cb-phone">Телефон *</label><input id="cb-phone" type="tel" name="phone" autocomplete="tel" placeholder="+7 ___ ___-__-__" required>'+
   '<label for="cb-what">Что нужно почистить</label><textarea id="cb-what" name="what" placeholder="Диван, матрас, ковёр…"></textarea>'+
   '<input class="cb-hp" type="text" name="_honey" tabindex="-1" autocomplete="off">'+
   '<label class="cb-agree"><input type="checkbox" name="agree" checked required> <span>Согласен на обработку персональных данных по <a href="privacy.html" target="_blank">политике конфиденциальности</a></span></label>'+
   '<button class="cb-send" type="submit">Жду звонка</button><div class="cb-err" aria-live="polite"></div></form></div>'+
   '<div class="cb-ok" hidden><div class="cb-ic">✅</div><h3>Заявка отправлена!</h3><p class="cb-sub">Алексей перезвонит вам в ближайшее время.</p></div></div>';
  function mount(){document.body.appendChild(m);}
  if(document.body)mount();else document.addEventListener('DOMContentLoaded',mount);

  var f=m.querySelector('form'),err=m.querySelector('.cb-err'),btn=m.querySelector('.cb-send'),ph=m.querySelector('#cb-phone');
  function open(e){if(e)e.preventDefault();var ws=document.getElementById('wsheet');if(ws)ws.classList.remove('open');
    m.querySelector('.cb-form-wrap').hidden=false;m.querySelector('.cb-ok').hidden=true;err.textContent='';
    m.classList.add('open');setTimeout(function(){ph.focus();},150);
    try{ym(113579876,'reachGoal','callback_open');}catch(_){}}
  function close(){m.classList.remove('open');}
  m.querySelector('.cb-x').onclick=close;
  m.addEventListener('click',function(e){if(e.target===m)close();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  document.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('[data-callback]');if(t)open(e);});

  // маска телефона +7 (999) 999-99-99
  ph.addEventListener('input',function(){var d=ph.value.replace(/\D/g,'');if(d[0]==='8')d='7'+d.slice(1);if(d[0]!=='7')d='7'+d;d=d.slice(0,11);
    var r='+7';if(d.length>1)r+=' ('+d.slice(1,4);if(d.length>=4)r+=')';if(d.length>4)r+=' '+d.slice(4,7);if(d.length>7)r+='-'+d.slice(7,9);if(d.length>9)r+='-'+d.slice(9,11);ph.value=r;});

  f.addEventListener('submit',function(e){
    e.preventDefault();err.textContent='';
    var digits=ph.value.replace(/\D/g,'');
    if(digits.length<11){err.textContent='Введите номер телефона полностью';ph.focus();return;}
    if(!f.agree.checked){err.textContent='Нужно согласие на обработку данных';return;}
    if(f._honey.value)return;
    var name=f.name.value.trim()||'не указано',what=f.what.value.trim()||'не указано';
    var now=new Date().toLocaleString('ru-RU',{timeZone:'Europe/Moscow',day:'2-digit',month:'long',hour:'2-digit',minute:'2-digit'});
    var data={
      '_subject':'📞 Клиент с сайта просит перезвонить: '+ph.value,
      '_template':'box',
      '_captcha':'false',
      '_honey':'',
      'Что случилось':'Клиент оставил заявку на сайте chisto-alexey.ru и просит связаться с ним',
      'Имя клиента':name,
      'Телефон':ph.value,
      'Что нужно почистить':what,
      'Когда отправлено':now+' (МСК)',
      'Страница':location.href
    };
    btn.disabled=true;btn.textContent='Отправляем…';
    fetch('https://formsubmit.co/ajax/'+TO,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
    .then(function(r){return r.json().catch(function(){return {success:r.ok};});})
    .then(function(j){
      try{console.log('[callback]',j);}catch(_){}
      var msg=String(j&&j.message||'');
      if(j&&(j.success===true||j.success==='true'||/activat/i.test(msg))){m.querySelector('.cb-form-wrap').hidden=true;m.querySelector('.cb-ok').hidden=false;f.reset();
        try{ym(113579876,'reachGoal','callback_sent');}catch(_){}}
      else throw 0;})
    .catch(function(e){try{console.log('[callback] error',e);}catch(_){} err.innerHTML='Не получилось отправить. Позвоните нам: <a href="tel:+79999662211">+7 999 966-22-11</a>';})
    .finally(function(){btn.disabled=false;btn.textContent='Жду звонка';});
  });
})();

/* уведомление о cookie: показывается один раз */
(function(){
  try{if(localStorage.getItem('cookieOk'))return;}catch(e){}
  var css='.ck-bar{position:fixed;left:50%;bottom:16px;transform:translate(-50%,20px);z-index:1050;width:calc(100% - 24px);max-width:720px;background:#0B2A3E;color:#E6F1F4;border:1px solid rgba(47,208,202,.35);border-radius:16px;padding:14px 16px;display:flex;align-items:center;gap:14px;box-shadow:0 12px 40px rgba(0,0,0,.35);font-size:.88rem;line-height:1.45;opacity:0;transition:.3s}'+
  '.ck-bar.show{opacity:1;transform:translate(-50%,0)}'+
  '.ck-bar a{color:#2FD0CA;text-decoration:underline}'+
  '.ck-ok{flex:none;border:0;border-radius:12px;padding:11px 20px;font:inherit;font-weight:800;background:#2FD0CA;color:#062A2A;cursor:pointer}'+
  '@media (max-width:600px){.ck-bar{flex-direction:column;align-items:stretch;gap:10px;bottom:10px;font-size:.82rem}.ck-ok{width:100%}}';
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
  function show(){
    var b=document.createElement('div');b.className='ck-bar';b.setAttribute('role','region');b.setAttribute('aria-label','Уведомление о cookie');
    b.innerHTML='<div>🍪 Мы используем файлы cookie и Яндекс Метрику, чтобы сайт работал удобнее. Продолжая пользоваться сайтом, вы соглашаетесь с <a href="privacy.html">политикой конфиденциальности</a>.</div><button type="button" class="ck-ok">Понятно</button>';
    document.body.appendChild(b);setTimeout(function(){b.classList.add('show');},400);
    b.querySelector('.ck-ok').onclick=function(){try{localStorage.setItem('cookieOk','1');}catch(e){}b.classList.remove('show');setTimeout(function(){b.remove();},300);};
  }
  if(document.body)show();else document.addEventListener('DOMContentLoaded',show);
})();

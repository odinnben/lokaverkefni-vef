%include('./sidur/header')  
  <header>
    <h1>{{skilabod}}</h1>
  </header>
  %include('./sidur/navbar',sida=None)
  <div class="container">
    <div class="boxVinnstri">
      %include('./sidur/nyjustu.tpl',myndir=nyjustmyndir,directors=nyjustdirectors,senur=nyjustsenur)
    </div>
    <div class="boxHaegri">
      <img src="/myndir/error404.png" width="100%">
    </div>
  </div>
%include('./sidur/footer')
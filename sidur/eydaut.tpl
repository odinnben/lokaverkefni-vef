%include('./sidur/header')  
  <header>
    <h1>Eyða</h1>
  </header>
  %include('./sidur/navbar',sida="eyda")
  <div class="container">
    <div class="boxVinnstri">
      %include('./sidur/nyjustu.tpl',myndir=nyjustmyndir,directors=nyjustdirectors,senur=nyjustsenur)
    </div>
    <div class="boxHaegri">
      <form method="post" class="bbuu" action="/eydamynd" accept-charset="ISO-8859-1">
        <input value={{mynd[0]}} name="myndid" type="hidden">
        <h3>Alveg viss um að eyða "<span class="ekkibold">{{mynd[1]}}</span>"</h3>
        <div class="ba su eyda">
          <input value="Já" type="submit" />
        </div>
      </form>
    </div>
  </div>
%include('./sidur/footer')
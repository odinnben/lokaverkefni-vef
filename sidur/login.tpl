%include('./sidur/header') 
  <header>
    <h1>Skrá inn</h1>
  </header>
  %include('./sidur/navbar',sida="login")
  <div class="container">
    <div class="boxVinnstri">
      %include('./sidur/nyjustu.tpl',myndir=nyjustmyndir,directors=nyjustdirectors,senur=nyjustsenur)
    </div>
    <div class="boxHaegri">
      <form method="post" class="bbuu" action="/login" accept-charset="ISO-8859-1">
        <div class="ba">
          <h3>Notandanafn</h3>
          <p><input name="notandanafn" type="text" required /></p>
        </div>
        <div class="ba">
          <h3>Lykilorð</h3>
          <p><input name="lykilord" type="password" required /></p>
        </div>
        <div class="ba su">
          <input value="Skrá inn" type="submit" />
        </div>
      </form>
    </div>
  </div>
%include('./sidur/footer')
%include('./sidur/header') 
  <header>
    <h1>Bæta Við</h1>
  </header>
  %include('./sidur/navbar',sida="bæta")
  <div class="container">
    <div class="boxVinnstri">
      %include('./sidur/nyjustu.tpl',myndir=nyjustmyndir,directors=nyjustdirectors,senur=nyjustsenur)
    </div>
    <div class="boxHaegri">
      <form method="post" class="bbuu" action="/baetavid" accept-charset="ISO-8859-1">
        <div class="ba">
          <h3>Titill</h3>
          <p><input name="titill" type="text" required /></p>
        </div>
        <div class="ba">
          <h3>Aldurstakmark</h3>
          <p>
            <select name="aldurstakmark">
              <option value="G">G - General - Audiences</option>
              <option value="PG">PG - Parental Guidance Suggested</option>
              <option value="PG-13">PG-13 - Parents Strongly Cautioned</option>
              <option value="R">R - Restricted</option>
              <option value="NC-17">NC-17 - Adults Only</option>
            </select>
          </p>
        </div>
        <div class="ba">
          <h3>Gefið Út</h3>
          <p><input name="gefidut" type="date" required /></p>
        </div>
        <div class="ba">
          <h3>Rating</h3>
          <p><input name="rating" type="number" placeholder="1 - 100" required /></p>
        </div>
        <div class="ba">
          <h3>Lengd</h3>
          <p><input name="lengd" type="number" placeholder="Í mínútum" required /></p>
        </div>
        <div class="ba">
          <h3>Framleiðslufyrirtæki</h3>
          <p><input name="framleidslu" type="text" placeholder="t.d. Marvel" required /></p>
        </div>
        <div class="ba">
          <h3>Myndarskjal</h3>
          <p><input name="myndarskjal" type="text" placeholder="t.d. mynd.png" required /></p>
        </div>
        <div class="ba">
          <h3>Trailer Youtube</h3>
          <p><input name="trailer" type="text" placeholder="t.d. sZs4NDC4yrI" required /></p>
        </div>
        <div class="ba">
          <h3>Sena/ur</h3>
          <p><input name="sena" type="text" placeholder="Fleiri en ein , á milli t.d. Action,Drama,Short" required /></p>
        </div>
        <div class="ba">
          <h3>Leikstjóri/ar</h3>
          <p><input name="leikstjori" type="text" placeholder="Fleiri en einn , á milli t.d. Einar,Óðinn,Matti" required /></p>
        </div>
        <div class="ba">
          <h3>Lýsing</h3>
          <p><textarea rows="7" name="lysing" placeholder="Sláðu inn stutta lýsingu..." required></textarea></p>
        </div>
        <div class="ba su">
          <input value="Bæta við" type="submit" />
        </div>
      </form>
    </div>
  </div>
%include('./sidur/footer')
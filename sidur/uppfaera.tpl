%include('./sidur/header') 
  <header>
    <h1>Uppfæra</h1>
  </header>
  %include('./sidur/navbar',sida="uppfæra")
  <div class="container">
    <div class="boxVinnstri">
      %include('./sidur/nyjustu.tpl',myndir=nyjustmyndir,directors=nyjustdirectors,senur=nyjustsenur)
    </div>
    <div class="boxHaegri">
      <form method="post" class="bbuu" action="/uppfaerabio" accept-charset="ISO-8859-1">
        <input value={{mynd[0]}} name="myndid" type="hidden">
        <div class="ba">
          <h3>Titill</h3>
          <p><input name="titill" type="text" value='{{mynd[1]}}' required /></p>
        </div>
        <div class="ba">
          <h3>Aldurstakmark</h3>
          <p>
            <select name="aldurstakmark">
              %aldur = ["","","","",""]
              %if mynd[2] == "G":aldur[0]="selected"
              %elif mynd[2] == "PG":aldur[1]="selected"
              %elif mynd[2] == "PG-13":aldur[2]="selected"
              %elif mynd[2] == "R":aldur[3]="selected"
              %elif mynd[2] == "NC-17":aldur[4]="selected"
              %end
              <option value="G" {{aldur[0]}}>G - General - Audiences</option>
              <option value="PG" {{aldur[1]}}>PG - Parental Guidance Suggested</option>
              <option value="PG-13" {{aldur[2]}}>PG-13 - Parents Strongly Cautioned</option>
              <option value="R" {{aldur[3]}}>R - Restricted</option>
              <option value="NC-17" {{aldur[4]}}>NC-17 - Adults Only</option>
            </select>
          </p>
        </div>
        <div class="ba">
          <h3>Gefið Út</h3>
          <p><input name="gefidut" type="date" value='{{mynd[3]}}' required /></p>
        </div>
        <div class="ba">
          <h3>Rating</h3>
          <p><input name="rating" type="number" placeholder="1 - 100" value='{{mynd[4]}}' required /></p>
        </div>
        <div class="ba">
          <h3>Lengd</h3>
          <p><input name="lengd" type="number" placeholder="Í mínútum" value='{{mynd[5]}}' required /></p>
        </div>
        <div class="ba">
          <h3>Framleiðslufyrirtæki</h3>
          <p><input name="framleidslu" type="text" placeholder="t.d. Marvel" value='{{mynd[6]}}' required /></p>
        </div>
        <div class="ba">
          <h3>Myndarskjal</h3>
          <p><input name="myndarskjal" type="text" placeholder="t.d. mynd.png" value='{{mynd[7]}}' required /></p>
        </div>
        <div class="ba">
          <h3>Trailer Youtube</h3>
          <p><input name="trailer" type="text" placeholder="t.d. sZs4NDC4yrI" value='{{mynd[8]}}' required /></p>
        </div>
        <div class="ba">
          <h3>Sena/ur</h3>
          <p><input name="sena" type="text" placeholder="Fleiri en ein , á milli t.d. Action,Drama,Short" value='{{senur}}' required /></p>
        </div>
        <div class="ba">
          <h3>Leikstjóri/ar</h3>
          <p><input name="leikstjori" type="text" placeholder="Fleiri en einn , á milli t.d. Einar,Óðinn,Matti" value='{{directors}}' required /></p>
        </div>
        <div class="ba">
          <h3>Lýsing</h3>
          <p><textarea rows="7" name="lysing" placeholder="Sláðu inn stutta lýsingu..." required>{{mynd[9]}}</textarea></p>
        </div>
        <div class="ba su">
          <input value="Uppfæra" type="submit" />
        </div>
      </form>
    </div>
  </div>
%include('./sidur/footer')
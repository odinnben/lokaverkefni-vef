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
      <h2>Veldu Mynd Til Að Eyða</h2>
      <div class="container_allar">
        %for x in range(len(myndir)):
          <div class="box_allar uppf" style="
          background: url('/myndir/{{myndir[x][7]}}');
          background-repeat: no-repeat;
          background-position: center;
          background-size:cover;
          ">
            <a class="utanum" href="/eydaut/{{myndir[x][0]}}">
              <div class="box2_allar">
                <div class="box3_allar">
                  <h2>{{myndir[x][1]}}</h2>
                </div>
              </div>
              
            </a>
          </div>
        %end
      </div>
    </div>
  </div>
%include('./sidur/footer')
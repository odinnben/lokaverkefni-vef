%include('./sidur/header')  
  <header>
    <h1>Leit</h1>
  </header>
  %include('./sidur/navbar',sida=None)
  <div class="container">
    <div class="boxVinnstri">
      %include('./sidur/nyjustu.tpl',myndir=nyjustmyndir,directors=nyjustdirectors,senur=nyjustsenur)
    </div>
    <div class="boxHaegri">
      <div class="container_allar">
      %if enginMynd:
        <h2>Leitar Niðurstöður Engar Fyrir <span class="leit"><strong>"</strong>{{leit}}<strong>"</strong></span></h2>
      %else:
        <h2>Leitar Niðurstöður <span class="leit"><strong>"</strong>{{leit}}<strong>"</strong></span></h2>
        %for x in range(len(myndir)):
          <div class="box_allar" style="
          background: url('/myndir/{{myndir[x][7]}}');
          background-repeat: no-repeat;
          background-position: center;
          background-size:cover;
          ">
            <a class="utanum" href="/kvikmynd/{{myndir[x][0]}}">
              <div class="box2_allar">
                <div class="rating">
                  <h3>Einkunn</h3>
                  <h4>{{myndir[x][4]}}<span class="hundrad">/100</span></h4>
                </div>
                <div class="box3_allar">
                  <h2>{{myndir[x][1]}}</h2>
                  <h4><span class="gefinut">Gefin út</span> {{myndir[x][3]}}</h4>
                </div>
              </div>
              <div class="nanar_allar">
                <h4>Sena</h4>
                <p>
                %for i in range(len(senur[x])):
                  %if len(senur[x]) == 1:
                    {{senur[x][i][1]}}
                  %elif i+1 == len(senur[x]):
                    & {{senur[x][i][1]}}
                  %elif i+2 == len(senur[x]):
                    {{senur[x][i][1]}}
                  %else:
                    {{senur[x][i][1]}},
                  %end
                %end
                </p>
                <h4>Leikstjórar</h4>
                <p>
                %for i in range(len(directors[x])):
                  %if len(directors[x]) == 1:
                    {{directors[x][i][1]}}
                  %elif i+1 == len(directors[x]):
                    & {{directors[x][i][1]}}
                  %elif i+2 == len(directors[x]):
                    {{directors[x][i][1]}}
                  %else:
                    {{directors[x][i][1]}},
                  %end
                %end
                </p>
                <h4>Aldurstakmark</h4>
                <p>{{myndir[x][2]}}</p>
                <h4>Lengd</h4>
                <p>{{myndir[x][5]}} min</p>
              </div>
            </a>
          </div>
        %end
      %end
      </div>
    </div>
  </div>
%include('./sidur/footer')
%include('./sidur/header') 
<style>
header {
   background-image: url("/myndir/{{mynd[7]}}");
   background-attachment: unset;
}
</style>
<header class="kvik">
  <h1>{{mynd[1]}}</h1>
  <h2> {{mynd[2]}} <span class="nanar">|</span> {{mynd[5]}}min <span class="nanar">|</span> 
    %for i in range(len(senur)):
      %if len(senur) == 1:
        {{senur[i][1]}}
      %elif i+1 == len(senur):
        & {{senur[i][1]}}
      %elif i+2 == len(senur):
        {{senur[i][1]}}
      %else:
        {{senur[i][1]}},
      %end
    %end
   <span class="nanar">|</span> {{mynd[3]}}</h2>
</header>
  %include('./sidur/navbar',sida=None)
<div class="container">
  <div class="boxVinnstri um">
    <div class="umMyndina">
      <h3>Sena</h3>
      <p>
      %for i in range(len(senur)):
        %if len(senur) == 1:
          {{senur[i][1]}}
        %elif i+1 == len(senur):
          & {{senur[i][1]}}
        %elif i+2 == len(senur):
          {{senur[i][1]}}
        %else:
          {{senur[i][1]}},
        %end
      %end
      </p>
      <h3>Leikstjórar</h3>
      <p>
      %for i in range(len(directors)):
        %if len(directors) == 1:
          {{directors[i][1]}}
        %elif i+1 == len(directors):
          & {{directors[i][1]}}
        %elif i+2 == len(directors):
          {{directors[i][1]}}
        %else:
          {{directors[i][1]}},
        %end
      %end
      </p>
      <h3>Aldurstakmark</h3>
      <p>{{mynd[2]}}</p>
      <h3>Lengd</h3>
      <p>{{mynd[5]}}min</p>
      <h3>Gefin út</h3>
      <p>{{mynd[3]}}</p>
    </div>
  </div>
  <div class="boxHaegri">
    <div class="trailer">
      <iframe width="100%" height="300px" src="https://www.youtube.com/embed/{{mynd[8]}}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
    <div class="umMyndina2">
      <h3>Um myndina</h3>
      <p>{{mynd[9]}}</p>
    </div>
  </div>
</div>
%include('./sidur/footer') 
<div class="navbar">
	<div class="vinnstri">
		%if sida == "Heim":
		<a href="/" class="active">Heim</a>
		%else:
		<a href="/">Heim</a>
		%end
		%if sida == "AllarKvikmyndir":
		<a href="/allarkvikmyndir" class="active">Allar Kvikmyndir</a>
		%else:
		<a href="/allarkvikmyndir">Allar Kvikmyndir</a>
		%end
	</div>
	<div class="haegri">
	%if nafn:
		%if sida == "bæta":
		<a href="/baeta" class="active">Bæta við</a>
		%else:
		<a href="/baeta">Bæta við</a>
		%end
		%if sida == "uppfæra":
		<a href="/uppfaera" class="active">Uppfæra</a>
		%else:
		<a href="/uppfaera">Uppfæra</a>
		%end
		%if sida == "eyda":
		<a href="/eyda" class="active">Eyða</a>
		%else:
		<a href="/eyda">Eyða</a>
		%end
		<a href="skraut">Skrá út</a>
	%else:
	    <div class="login">
	    %if sida == "login":
	      <a href="/skrainn" class="active">Skrá inn</a>
	    %else:
	      <a href="/skrainn">Skrá inn</a>
	    %end
	    </div>
	%end
	</div>
</div>
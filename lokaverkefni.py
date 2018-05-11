from bottle import *
import os, datetime
from locale import *
from beaker.middleware import SessionMiddleware
from database import *
setlocale(LC_TIME,"is-IS")
session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

@route("/")
def index():
    s = request.environ.get('beaker.session')
    nafn = None
    if s.get("notandi"):
        nafn = s["notandi"][0]
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    bestmyndir = hl.bestu2018()
    bestsenur = []
    bestdirectors = []
    for x in range(len(bestmyndir)):
        bestmyndir[x][3] = bestmyndir[x][3].strftime('%e. %B %Y')
    for x in bestmyndir:
        bestdir = []
        for i in hl.dirMynd(x[0]):
            bestdir.append(hl.finnaDir(i[1]))
        bestdirectors.append(bestdir)
        bestsen = []
        for i in hl.senurMynd(x[0]):
            bestsen.append(hl.finnaSenu(i[1]))
        bestsenur.append(bestsen)
    return template("./sidur/index",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,myndir = bestmyndir,senur = bestsenur,directors=bestdirectors)

@route("/kvikmynd/<myndid>")
def kvikmynd(myndid):
    s = request.environ.get('beaker.session')
    nafn = None
    if s.get("notandi"):
        nafn = s["notandi"][0]
    hl = saekjaGogn()
    mynd = hl.finnaMynd(myndid)
    directors = []
    for x in hl.dirMynd(myndid):
        directors.append(hl.finnaDir(x[1]))
    senur = []
    for x in hl.senurMynd(myndid):
        senur.append(hl.finnaSenu(x[1]))
    mynd[3] = mynd[3].strftime('%e. %B %Y')
    return template("./sidur/kvikmynd",nafn=nafn,mynd = mynd,directors = directors,senur = senur)

@route("/allarkvikmyndir")
def allarkvikmyndir():
    s = request.environ.get('beaker.session')
    nafn = None
    if s.get("notandi"):
        nafn = s["notandi"][0]
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    myndir = hl.allarMyndir()
    directors = []
    senur = []
    for x in range(len(myndir)):
        myndir[x][3] = myndir[x][3].strftime('%e. %B %Y')
    for x in myndir:
        dir = []
        for i in hl.dirMynd(x[0]):
            dir.append(hl.finnaDir(i[1]))
        directors.append(dir)
        sen = []
        for i in hl.senurMynd(x[0]):
            sen.append(hl.finnaSenu(i[1]))
        senur.append(sen)
    return template("./sidur/allarmyndir",nafn=nafn,myndir = myndir,directors = directors,senur = senur,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur)

@route("/leit")
def leit():
    s = request.environ.get('beaker.session')
    nafn = None
    if s.get("notandi"):
        nafn = s["notandi"][0]
    leit = request.params.get('leita')
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    myndir = hl.leitMynd(leit)
    directors = []
    senur = []
    if myndir:
        for x in range(len(myndir)):
            myndir[x][3] = myndir[x][3].strftime('%e. %B %Y')
        for x in myndir:
            dir = []
            for i in hl.dirMynd(x[0]):
                dir.append(hl.finnaDir(i[1]))
            directors.append(dir)
            sen = []
            for i in hl.senurMynd(x[0]):
                sen.append(hl.finnaSenu(i[1]))
            senur.append(sen)
        return template("./sidur/leita",nafn=nafn,leit=leit,enginMynd=False,myndir = myndir,directors = directors,senur = senur,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur)
    else:
        return template("./sidur/leita",nafn=nafn,leit=leit,enginMynd=True,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur)

@route("/skrainn")
def skrainn():
    nafn = None
    s = request.environ.get('beaker.session')
    if s.get("notandi"):
        return redirect("/")
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    return template("./sidur/login",nafn=nafn,nyjustmyndir=nyjustmyndir,nyjustsenur=nyjustsenur,nyjustdirectors=nyjustdirectors)

@post("/login")
def login():
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    s = request.environ.get('beaker.session')
    notandi = request.forms.get('notandanafn')
    lykil = request.forms.get('lykilord')
    hl = saekjaGogn()
    notandinn = hl.admin(notandi,lykil)
    s['notandi'] = notandinn
    if notandinn == None:
        nafn = None
        return template("./sidur/annad",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,skilabod = "Notandi eða lykilorð vitlaust")
    return redirect("/")

@route("/skraut")
def skraut():
    s = request.environ.get('beaker.session')
    s.delete()
    return redirect("/")

@route("/eyda")
def eydaaa():
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    s = request.environ.get('beaker.session')
    if s.get("notandi"):
        nafn = s["notandi"][0]
    else:
        nafn = None
        return template("./sidur/annad",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,skilabod = "Aðgangur Lokaður")
    myndir = hl.allarMyndir()
    directors = []
    senur = []
    for x in range(len(myndir)):
        myndir[x][3] = myndir[x][3].strftime('%e. %B %Y')
    for x in myndir:
        dir = []
        for i in hl.dirMynd(x[0]):
            dir.append(hl.finnaDir(i[1]))
        directors.append(dir)
        sen = []
        for i in hl.senurMynd(x[0]):
            sen.append(hl.finnaSenu(i[1]))
        senur.append(sen)
    return template("./sidur/eyda",nafn=nafn,myndir = myndir,directors = directors,senur = senur,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur)

@route("/eydaut/<myndid>")
def eydaut(myndid):
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    s = request.environ.get('beaker.session')
    if s.get("notandi"):
        nafn = s["notandi"][0]
    else:
        nafn = None
        return template("./sidur/annad",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,skilabod = "Aðgangur Lokaður")
    mynd = hl.finnaMynd(myndid)
    return template("./sidur/eydaut",nafn=nafn,mynd = mynd,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur)

@post("/eydamynd")
def eydamyndinni():
    myndid = request.forms.get('myndid')
    hl = saekjaGogn()
    ed = eyda()
    senur = hl.senurMynd(myndid)
    for x in senur:
        ed.senu(myndid,x[1])
    dir = hl.dirMynd(myndid)
    for x in dir:
        ed.director(myndid,x[1])
    eydaa = ed.biomynd(myndid)
    return redirect("/")

@route("/baeta")
def baeta():
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    s = request.environ.get('beaker.session')
    if s.get("notandi"):
        nafn = s["notandi"][0]
    else:
        nafn = None
        return template("./sidur/annad",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,skilabod = "Aðgangur Lokaður")
    return template("./sidur/baeta",nafn=nafn,nyjustmyndir=nyjustmyndir,nyjustsenur=nyjustsenur,nyjustdirectors=nyjustdirectors)

@post("/baetavid")
def baetavid():
    titill = request.forms.get('titill')
    aldurstakmark = request.forms.get('aldurstakmark')
    gefidut = request.forms.get('gefidut')
    rating = request.forms.get('rating')
    lengd = request.forms.get('lengd')
    framleidslu = request.forms.get('framleidslu')
    myndarskjal = request.forms.get('myndarskjal')
    trailer = request.forms.get('trailer')
    sena = request.forms.get('sena')
    leikstjori = request.forms.get('leikstjori')
    lysing = request.forms.get('lysing')
    if "," in sena:
        sena = sena.split(",")
    else:
        sena = [sena]
    if "," in leikstjori:
        leikstjori = leikstjori.split(",")
    else:
        leikstjori = [leikstjori]
    hl = baetaVid()
    myndID = hl.biomynd(titill,aldurstakmark,gefidut,rating,lengd,framleidslu,myndarskjal,trailer,lysing)
    for x in sena:
        if x[0] == " ":
            x = x[1::]
        hl.senu(myndID,x)
    for x in leikstjori:
        if x[0] == " ":
            x = x[1::]
        hl.director(myndID,x)
    return redirect("/")

@route("/uppfaera")
def uppfaeraa():
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    s = request.environ.get('beaker.session')
    if s.get("notandi"):
        nafn = s["notandi"][0]
    else:
        nafn = None
        return template("./sidur/annad",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,skilabod = "Aðgangur Lokaður")
    myndir = hl.allarMyndir()
    directors = []
    senur = []
    for x in range(len(myndir)):
        myndir[x][3] = myndir[x][3].strftime('%e. %B %Y')
    for x in myndir:
        dir = []
        for i in hl.dirMynd(x[0]):
            dir.append(hl.finnaDir(i[1]))
        directors.append(dir)
        sen = []
        for i in hl.senurMynd(x[0]):
            sen.append(hl.finnaSenu(i[1]))
        senur.append(sen)
    return template("./sidur/uppf",nafn=nafn,myndir = myndir,directors = directors,senur = senur,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur)

@route("/uppfaeramynd/<myndid>")
def uppfaeramynd(myndid):
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    s = request.environ.get('beaker.session')
    if s.get("notandi"):
        nafn = s["notandi"][0]
    else:
        nafn = None
        return template("./sidur/annad",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,skilabod = "Aðgangur Lokaður")
    mynd = hl.finnaMynd(myndid)
    senur = ""
    for x in hl.senurMynd(myndid):
        if len(senur) == 0:
            senur += hl.finnaSenu(x[1])[1]
        else:
            senur += ","+hl.finnaSenu(x[1])[1]
    directors = ""
    for x in hl.dirMynd(myndid):
        if len(directors) == 0:
            directors += hl.finnaDir(x[1])[1]
        else:
            directors += ","+hl.finnaDir(x[1])[1]
    return template("./sidur/uppfaera",nafn=nafn,mynd = mynd,directors = directors,senur = senur,nyjustmyndir=nyjustmyndir,nyjustdirectors=nyjustdirectors,nyjustsenur=nyjustsenur)

@post("/uppfaerabio")
def uppfaerabio():
    myndID = request.forms.get('myndid')
    titill = request.forms.get('titill')
    aldurstakmark = request.forms.get('aldurstakmark')
    gefidut = request.forms.get('gefidut')
    rating = request.forms.get('rating')
    lengd = request.forms.get('lengd')
    framleidslu = request.forms.get('framleidslu')
    myndarskjal = request.forms.get('myndarskjal')
    trailer = request.forms.get('trailer')
    sena = request.forms.get('sena')
    leikstjori = request.forms.get('leikstjori')
    lysing = request.forms.get('lysing')
    if "," in sena:
        tmpSena = sena.split(",")
    else:
        tmpSena = [sena]
    if "," in leikstjori:
        tmpleikstjori = leikstjori.split(",")
    else:
        tmpleikstjori = [leikstjori]
    sena = []
    for x in tmpSena:
        if x[0] == " ":
            x = x[1::]
        sena.append(x)
    leikstjori = []
    for x in tmpleikstjori:
        if x[0] == " ":
            x = x[1::]
        leikstjori.append(x)
    hl = saekjaGogn()
    gsenur = []
    for x in hl.senurMynd(myndID):
        gsenur.append(hl.finnaSenu(x[1]))
    gleikstjori = []
    for x in hl.dirMynd(myndID):
        gleikstjori.append(hl.finnaDir(x[1]))
    hl = eyda()
    sentil = []
    for x in gsenur:
        if x[1] not in sena:
            hl.senu(myndID,x[0])
        else:
            sentil.append(x[1])
    leikstjoritil = []
    for x in gleikstjori:
        if x[1] not in leikstjori:
            hl.director(myndID,x[0])
        else:
            leikstjoritil.append(x[1])
    hl = uppfaera()
    hl.biomynd(titill,aldurstakmark,gefidut,rating,lengd,framleidslu,myndarskjal,trailer,lysing,myndID)
    hl = baetaVid()
    for x in sena:
        if x not in sentil:
            hl.senu(myndID,x)
    for x in leikstjori:
        if x not in leikstjoritil:
            hl.director(myndID,x)
    return redirect("/")

@route('/css/<skjal>')
def server_static(skjal):
    return static_file(skjal, root='./css')

@route('/myndir/<skjal>')
def server_static(skjal):
    return static_file(skjal, root='./myndir')

@error(404)
def villa404(error):
    s = request.environ.get('beaker.session')
    nafn = None
    if s.get("notandi"):
        nafn = s["notandi"][0]
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    return template("./sidur/annad",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,skilabod = "Villa 404: Síða fannst ekki")

@error(500)
def villa500(error):
    s = request.environ.get('beaker.session')
    nafn = None
    if s.get("notandi"):
        nafn = s["notandi"][0]
    hl = saekjaGogn()
    nyjustmyndir = hl.nyjustu()
    nyjustsenur = []
    nyjustdirectors = []
    for x in range(len(nyjustmyndir)):
        nyjustmyndir[x][3] = nyjustmyndir[x][3].strftime('%e. %B %Y')
    for x in nyjustmyndir:
        nyjustdir = []
        for i in hl.dirMynd(x[0]):
            nyjustdir.append(hl.finnaDir(i[1]))
        nyjustdirectors.append(nyjustdir)
        nyjustsen = []
        for i in hl.senurMynd(x[0]):
            nyjustsen.append(hl.finnaSenu(i[1]))
        nyjustsenur.append(nyjustsen)
    return template("./sidur/annad",nafn=nafn,nyjustmyndir = nyjustmyndir,nyjustdirectors = nyjustdirectors, nyjustsenur = nyjustsenur,skilabod = "Villa 500")

#run(host="0.0.0.0", port=os.environ.get('PORT'), app=app)
run(host='localhost', port=8080, app=app, debug=True, reloader=True)
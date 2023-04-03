from multiprocessing import context
from sre_constants import NOT_LITERAL_IGNORE
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime

from App.models import *

# Create your views here.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
def accueill(request):
    if request.user.is_authenticated:
        ann = AnneScolaire.objects.latest('ann_sco_nom')
        x = ann.ann_sco_nom
        
        totale = Etudiant.objects.filter(an_sco=x).count()
        femme = Etudiant.objects.filter(sexe_etu='Femine',an_sco=x).count()
        homme = Etudiant.objects.filter(sexe_etu='Masculin',an_sco=x).count()
        tab = Etudiant.objects.filter(an_sco=x).order_by('-id')[:5]

        

        context = {
            'tt': totale,
            'hm': homme,
            'fm': femme,
            'tb': tab,
            #'con': con
        }
        return render(request, 'acceill.html', context)
    else:
        return redirect('/')
  
def add_etu(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            etu = Etudiant()
            #ag = Agent()
           # fr = Frais()
            
            etu.nom_etu = request.POST.get('nom')
            etu.nni_etu = request.POST.get('nni_etu')
            if request.POST.get('dateNai') != "":
                etu.dt_nai_etu = request.POST.get('dateNai')
            else:
                etu.dt_nai_etu = datetime.now().strftime('%Y-%m-%d')
            etu.dt_iscri_etu = datetime.now().strftime('%Y-%m-%d')
            etu.sexe_etu = request.POST.get('sexe_etu')
            if request.POST.get('fraisInsc_etu') != "":
                etu.fraisInsc_etu = request.POST.get('fraisInsc_etu')
            if request.POST.get('fraisFixe_etu') != "":
                etu.fraisFixe_etu = request.POST.get('fraisFixe_etu')
            etu.classe_etu = request.POST.get('classe_etu')
            etu.an_sco = request.POST.get('annee_scolair')
            if request.POST.get('rim_etu'):
                etu.etu_rim = request.POST.get('rim_etu')
            #etu.nom_ag = request.POST.get('nom_agent')
            etu.conn_ag = request.POST.get('conn_agent')

            if len(request.FILES) !=0:
                etu.image_etu = request.FILES['etu_photo']

            etu.save()
            '''
            ag.nom_ag = request.POST.get('nom_agent')
            ag.num_ag = request.POST.get('num_agent')

            ag.save()
            
            fr.etu = request.POST.get('nom') +" "+ request.POST.get('prenom')
            fr.dt_pay =  datetime.now().strftime('%Y-%m-%d')
            fr.prix = request.POST.get('frai_ins')
            fr.ann_sco = request.POST.get('annee_scolair')
        
            fr.save() 
            '''

            messages.success(request, f'l\'etudiant {etu.nom_etu} a bien inscri ')
            redirect('/')



        reg = ('Adrar','Assaba','Brakna','Nouadhibou','Gorgol','Trarza','Guidimakha','Hodh El Chargui','Hodh El Gharbi','Inchiri','Tiris Wamomur','Tagant','Nouakchott')
        sx = ('Masculin','Femine')
        cl = Etu_classe.objects.all()
        ann = AnneScolaire.objects.latest('ann_sco_nom')
        
        context = {
            'cl': cl,
            'x': sx, 
            'wil': reg,
            'an': ann
        }
        return render(request, 'add_etu.html',context)
    else:
        return redirect('/')

def supEtu(request, id):
    if request.user.is_authenticated:
        etu = Etudiant.objects.get(id=id)
        x = etu.classe_etu

        cl = Etu_classe.objects.get(class_nom=x)
        id = cl.id

        etu.delete()

        return redirect('unClass', id=id)
    else:
        return redirect('/')

def UP(request, id):
    if request.user.is_authenticated:
        etu = Etudiant.objects.get(id=id)
        x = etu.classe_etu
        if request.method == "POST":
            if len(request.FILES) != 0:
                if etu.image_etu:
                    if len(etu.image_etu) > 0:
                        os.remove(etu.image_etu.path)
                etu.image_etu = request.FILES['image_etu']

            etu.nom_etu = request.POST.get('nom')
            etu.nni_etu = request.POST.get('nni_etu')
            if request.POST.get('dateNai') != "":
                etu.dt_nai_etu = request.POST.get('dateNai')
            #etu.dt_nai_etu = request.POST.get('dateNai')
            etu.sexe_etu = request.POST.get('sexe_etu')
            etu.classe_etu = request.POST.get('classe_etu')
            etu.an_sco = request.POST.get('annee_scolair')
            etu.conn_ag = request.POST.get('conn_agent')
            etu.fraisInsc_etu = request.POST.get('fraisInsc_etu')
            etu.fraisFixe_etu = request.POST.get('fraisFixe_etu')

            etu.save()
            messages.success(request, f'l\'etudiant {etu.nom_etu} a bien Modifier ')
            
            cl = Etu_classe.objects.get(class_nom=x)
            id = cl.id
            return redirect('unClass', id=id)





        context = {
            'etu': etu,
        }
        return render(request, 'updqte_etu.html',context)
    else:
        return redirect('/')

def add_emp(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            emp = Employe()
            #ag = Agent()
           # fr = Frais()
            
            emp.nom_emp = request.POST.get('nom_emp')
          #  emp.nni_emp = request.POST.get('nni_emp')
            emp.fonc_emp = request.POST.get('fon_emp')
            emp.num_tel_emp = request.POST.get('conn_emp')
           # emp.credit_emp = request.POST.get('cr_emp')
            emp.salair_emp = request.POST.get('sr_emp')
            emp.date_rc = datetime.now().strftime('%Y-%m-%d')

            emp.save()
            '''
            ag.nom_ag = request.POST.get('nom_agent')
            ag.num_ag = request.POST.get('num_agent')

            ag.save()
            
            fr.etu = request.POST.get('nom') +" "+ request.POST.get('prenom')
            fr.dt_pay =  datetime.now().strftime('%Y-%m-%d')
            fr.prix = request.POST.get('frai_ins')
            fr.ann_sco = request.POST.get('annee_scolair')
        
            fr.save() 
            '''

            messages.success(request, f'l\'employee {emp.nom_emp} a bien ajoute ')
            redirect('/')


        tmp = Employe.objects.all().count()
        emp = Employe.objects.all()
        cl = Metier.objects.all()      
        context = {
            'cl': cl,
            'emp' : emp,
            'tmp' : tmp
        }
        return render(request, 'add_emp.html',context)
    else:
        return redirect('/')

def classes(request):
    if request.user.is_authenticated:
        ann = AnneScolaire.objects.latest('ann_sco_nom')
        x = ann.ann_sco_nom
        
        7#cls = Etu_classe.objects.filter(ann_sco=x).order_by('id')[:1]
        tc = Etu_classe.objects.filter(ann_sco=x)

        id= tc[0].id
        return redirect('unClass', id=id)
        
    else:
        return redirect('/')   

def Dep(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            dp = Depence()

            dp.naturDep = request.POST.get('nature')
            if request.POST.get('dateOperation') != "":
                dp.dateDep = request.POST.get('dateOperation')
            else:
                dp.dateDep = datetime.now().strftime('%Y-%m-%d')
            if request.POST.get('montant') != "":
                dp.montanDep = request.POST.get('montant')

            dp.save()
            messages.success(request, f'vous avez fait une opération {dp.naturDep} avec  succe')
            redirect('/')

        tp = ('salaire-employé','facture d\'électricité','facture d\'au','Autre')
        ttdp = Depence.objects.all()
        b = 0
        for i in ttdp:
            b = b + i.montanDep
    
        context = {
            'tp':tp,
            'b':b,
            'ttdp':ttdp
        }
        return render(request, 'Dep.html',context)

        
    else:
        return redirect('/')   

def GSP(request):
    if request.user.is_authenticated:
        ann = AnneScolaire.objects.latest('ann_sco_nom')
        x = ann.ann_sco_nom
        
        7#cls = Etu_classe.objects.filter(ann_sco=x).order_by('id')[:1]
        tc = Etu_classe.objects.filter(ann_sco=x)

        id= tc[0].id
        return redirect('EtuP', id=id)
        
    else:
        return redirect('/')   

def Plus(request):
    if request.user.is_authenticated:
        ann = AnneScolaire.objects.latest('ann_sco_nom')
        x = ann.ann_sco_nom

        an = AnneScolaire.objects.all()
        cl = Etu_classe.objects.filter(ann_sco=x)
        arg = Frais.objects.all()
        et = Etudiant.objects.all()
        b = 0
        for i in et:
            b = b + i.fraisInsc_etu
        
        c=0
        for i in arg:
            c = c + i.prix

        c = c + b 
        mt = Metier.objects.all()
        if cl:
            context = {
            'an':  an,
            'cl':cl,
            'c':c,
            'mt':mt
            }
        else:
            context = {
            'an':  an,
            'mt':mt
            }
            

        
        return render(request, 'Plus.html', context)
    else:
        return redirect('/')

def Ann(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ann = AnneScolaire()
            ann.ann_sco_nom = request.POST.get('ann')
            ann.save()
        # return HttpResponse('/Plus/')
            return redirect('/Plus/')

        return render(request, 'add_anne.html')
    else:
        return redirect('/')

'''def Matiers(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            mtr = Matier()
            mtr.matier_nom = request.POST.get('mtr')
            mtr.save()
            # return HttpResponse('/Plus/')
            return redirect('/Plus/')

        return render(request, 'matier.html')
    else:
        return redirect('/')
'''
def ADD(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            mt = Metier()
            mt.matier_nom = request.POST.get('newmtr')
            mt.save()
        # return HttpResponse('/Plus/')
            return redirect('/Plus/')


       
        return render(request, 'ADD.html')
    else:
        return redirect('/')
def Clss(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            cl = Etu_classe()
            cl.ann_sco = request.POST.get('an_sc')
            cl.class_nom = request.POST.get('cls')
            cl.save()
        # return HttpResponse('/Plus/')
            return redirect('/Plus/')

        ann = AnneScolaire.objects.latest('ann_sco_nom')
        an = ann.ann_sco_nom

        context = {
            'an': an
        }
        return render(request, 'Clss.html', context)
    else:
        return redirect('/')

def unClass(request, id):
    if request.user.is_authenticated:
        cls = Etu_classe.objects.get(id=id)
        etu = Etudiant.objects.filter(classe_etu=cls.class_nom)
        oth = Etu_classe.objects.all()
        cll = Etu_classe.objects.get(id=id)
        x = cll.class_nom

        #etu_g = Etudiant.objects.values_list('nom_ag', flat=True)

        context = {
            'etu': etu,
            'oth': oth,
            'x': x,
            #'etu_g': etu_g
        }
        return render(request, 'sepa.html', context)
    else:
        return redirect('/')

def EtuP(request, id):
    if request.user.is_authenticated:
        cls = Etu_classe.objects.get(id=id)
        etu = Etudiant.objects.filter(classe_etu=cls.class_nom)
        oth = Etu_classe.objects.all()
        cll = Etu_classe.objects.get(id=id)
        x = cll.class_nom

        ttF = Frais.objects.filter(etuClasse=x)
        a = 0 
        for i in ttF:
            a = a + i.prix

        pri = 0 
        #etu_g = Etudiant.objects.values_list('nom_ag', flat=True)
        fri = Frais.objects.all()
        arg = Frais.objects.all()
        et = Etudiant.objects.all()
        b = 0
        for i in et:
            b = b + i.fraisInsc_etu
        
        c=0
        for i in arg:
            c = c + i.prix

        c = c + b 

        context = {
            'etu': etu,
            'oth': oth,
            'x': x,
            'a': a,
            'pri': pri,
            'fri': fri,
            'c': c
        }
        return render(request, 'paim.html', context)
    else:
        return redirect('/')

def detail(request, id):
    if request.user.is_authenticated:
        etu = Etudiant.objects.filter(id=id)
        context = {
            'etu': etu
        }
        return render(request, 'detail.html', context)
    else:
        return redirect('/')

'''def Abs(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            abs = Absence()
            abs.ann_sco = request.POST.get('an_sc')
            abs.etu_id = request.POST.get('id_etu')
            abs.dt_abs = request.POST.get('Abs-dt')
            abs.justification = request.POST.get('Jus')

            abs.save()
            et = Etudiant.objects.get(id=id)
            cl = et.classe_etu
            
            Id = Etu_classe.objects.filter(class_nom=cl)
            u = Id[0].id
            return redirect('Abs', id=id)

        ann = AnneScolaire.objects.latest('ann_sco_nom')
        x = ann.ann_sco_nom
        list = Absence.objects.filter(etu_id=id)
        jus = ('Justifier','Non justifier')
        etu = Etudiant.objects.get(id=id)
        context = {
            'list': list,
            'etu': etu,
            'x': x,
            'jus': jus

        }

        return render(request, 'Abs.html', context)
    else:
        return redirect('/')


def ListAbs(request, id):
    if request.user.is_authenticated:
        list = Absence.objects.filter(etu_id=id)
        etu = Etudiant.objects.get(id=id)

        context = {
            'list': list,
            'etu': etu
        }

        return render(request, 'ListAbs.html', context)
    else:
        return redirect('/')

def Notes(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            note = Note()
            note.etu_nt = request.POST.get('etu_id')
            note.an_nt = request.POST.get('ann_sc')
            note.cl_nt = request.POST.get('cl_ac')
            note.matier_nt = request.POST.get('matier')
            note.dev_nt =  request.POST.get('dev')
            note.ex_nt = request.POST.get('ex')

            note.save()
            return redirect('Notes', id=id)

        nt = Note.objects.filter(etu_nt=id)
        etu = Etudiant.objects.get(id=id)

        ann = AnneScolaire.objects.latest('ann_sco_nom')
        an = ann.ann_sco_nom

        x = Matier.objects.all()
        context = {
            'etu':etu,
            'an': an,
            'x': x,
            'nt': nt
            }

        return render(request, 'Note.html',context)
    else:
        return redirect('/')
 
def supNot(request, id):
    if request.user.is_authenticated:
        nt = Note.objects.get(id=id)
        x = nt.etu_nt

        nt.delete()
        return redirect('Notes', id=x)
    else:
        return redirect('/')

def supAbs(request, id):
    if request.user.is_authenticated:
        ab = Absence.objects.get(id=id)
        x = ab.etu_id

        ab.delete()
        return redirect('Abs', id=x)
    else:
        return redirect('/')
'''
def Paiment(request, id):
    if request.user.is_authenticated:
        etu = Etudiant.objects.get(id=id)

        fr = Frais.objects.filter(etu=id)

        context
        return render(request, 'Paiment.html', {'fr':fr,'etu':etu})
    else:
        return redirect('/')
    

def Pay(request, id):
    if request.user.is_authenticated:
        etu = Etudiant.objects.get(id=id)
        fr = Frais()
        fr.etu = id
        fr.etuClasse = etu.classe_etu
        fr.prix = etu.fraisFixe_etu
        fr.dt_pay = datetime.now().strftime('%Y-%m-%d')

        fr.save()

        

        messages.success(request, f'l\'etudiant {etu.nom_etu} a viens de Payer ')


        x = etu.classe_etu
        etu.nbrPay = etu.nbrPay + 1

        etu.save()

        cl = Etu_classe.objects.get(class_nom=x)
        id = cl.id
        return redirect('EtuP', id=id)

        etu = Etudiant.objects.get(id=id)
        x =etu.nom_etu
        y = etu.prenom_etu
        z = x+y

        ann = AnneScolaire.objects.latest('ann_sco_nom')
        an = ann.ann_sco_nom

        context = {
            'an': an,
            'z':z
        }

        return render(request, 'Pay.html', context)
    else:
        return redirect('/')

def Return(request, id):
    if request.user.is_authenticated:        
        etu = Etudiant.objects.get(id=id)       
        x = etu.classe_etu

        cl = Etu_classe.objects.get(class_nom=x)
        id = cl.id
        return redirect('EtuP', id=id)

    else:
        return redirect('/')

def ReturnClasse(request, id):
    if request.user.is_authenticated:        
        etu = Etudiant.objects.get(id=id)       
        x = etu.classe_etu

        cl = Etu_classe.objects.get(class_nom=x)
        id = cl.id
        return redirect('unClass', id=id)

    else:
        return redirect('/')
    
def Credite(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            dp = Depence()
            emp = Employe.objects.get(id=id)

            dp.naturDep = request.POST.get('empC')
            if request.POST.get('dateOperation') != "":
                dp.dateDep = request.POST.get('dtC')
            else:
                dp.dateDep = datetime.now().strftime('%Y-%m-%d')
            if request.POST.get('montant') != "":
                dp.montanDep = request.POST.get('monC')
                if int(dp.montanDep) > emp.salair_emp:
                    messages.success(request, f'Imposibele de faire cette opération')
                    tmp = Employe.objects.all().count()
                    emp = Employe.objects.all()
                    cl = Metier.objects.all()      
                    context = {
                        'cl': cl,
                        'emp' : emp,
                        'tmp' : tmp
                    }
                    return render(request, 'add_emp.html',context)
                    
            
            dp.save()

       
            emp.credit_emp = dp.montanDep
            emp.salair_emp = emp.salair_emp - int(dp.montanDep)
            emp.save()

            messages.success(request, f'vous avez fait une opération {dp.naturDep} avec succe')
            
            tmp = Employe.objects.all().count()
            emp = Employe.objects.all()
            cl = Metier.objects.all()      
            context = {
                'cl': cl,
                'emp' : emp,
                'tmp' : tmp
            }
            return render(request, 'add_emp.html',context)

        emp = Employe.objects.get(id=id)

        context = {
            'emp':emp
        }
        return render(request,'Credite.html',context)
    else:
        return redirect('/')

def SalaireEmp(request, id):
    if request.user.is_authenticated:
        emp = Employe.objects.get(id=id)
        dp = Depence()

        dp.montanDep = emp.salair_emp
        dp.dateDep = datetime.now().strftime('%Y-%m-%d')
        dp.naturDep = f'Salaire-employé : {emp.nom_emp }-{emp.fonc_emp}'
        

        dp.save()

        emp.salair_emp = emp.salair_emp + emp.credit_emp
        emp.credit_emp = 0 
        emp.save()

        messages.success(request, f'l\'employé {emp.nom_emp}-{emp.fonc_emp} a recvoir son salaire ')
        
        tmp = Employe.objects.all().count()
        emp = Employe.objects.all()
        cl = Metier.objects.all()      
        context = {
            'cl': cl,
            'emp' : emp,
            'tmp' : tmp
        }
        return render(request, 'add_emp.html',context)
    else:
        return redirect('/')




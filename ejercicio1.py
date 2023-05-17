
superficie1=23890
superficie2=48583
superficie=superficie1,superficie2

region="Biobio"
region1="Los_Lagos"

habitantes1=1556805 
habitantes2=828708
habitantes=habitantes1,habitantes2

dict={
    8:[region,superficie1,habitantes1],
    10:[region1,superficie2,habitantes2]
}
print(dict)

#densidad= round(habitantes/superficie)

dict[8]=capitalbio=["concepcion"]
dict[10]=capitallag=["puerto montt"]
capital=capitalbio,capitallag

dict[8]=comunasbio=["lota","lebu","los angeles"]
dict[10]= comunaslag=["castro","puerto varas","purranque"]
comunas=comunasbio,comunaslag

dict[8]=provinciasbio=("bio-bio","arauco","concepcion")
dict[10]=provinciaslag=("osorno","llanquihue","chiloé","palena")
provincias=provinciasbio,provinciaslag

#print(f"Nuevo diccionario: {dict}")

from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
W,H=1080,1350; NAVY=(20,35,52); GOLD=(190,145,55); WHITE=(248,248,246); DARK=(35,42,48)
out=Path('linkedin'); out.mkdir(exist_ok=True)
bp='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; fp='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
T=ImageFont.truetype(bp,72); B=ImageFont.truetype(fp,40); BR=ImageFont.truetype(bp,36); S=ImageFont.truetype(fp,30)
posts=[('Diagnóstico que impulsa decisiones',['Entender tu negocio es el primer paso para hacerlo crecer.','Detectamos lo que hoy te está costando resultados.\n\nProcesos · Costos · Comercialización · Rentabilidad','Información clara para decidir mejor y crecer con foco.\n\nTransformamos datos en decisiones que impulsan tu negocio.']),('Datos que se convierten en decisiones',['No se trata de tener datos. Se trata de saber qué hacer con ellos.','Analizamos tu negocio para encontrar patrones y oportunidades.\n\nIndicadores clave · Tendencias · Desempeño real','Decisiones posibles, resultados medibles, crecimiento sostenible.\n\nInformación confiable para decidir.']),('Lo que no medís, no lo podés mejorar',['Medir es el punto de partida para crecer.','Te ayudamos a identificar qué medir y cómo hacerlo.\n\nIndicadores clave · Procesos críticos · Resultados reales','Medir mejor es decidir mejor y crecer más.\n\nConvertimos números en acciones con impacto.']),('Menos supuestos, más claridad',['Reemplazar suposiciones por información confiable cambia la forma de decidir.','Analizamos tu negocio con una mirada externa y objetiva.\n\nSin sesgos · Con metodología · Con foco en resultados','Claridad para decidir, enfoque para crecer, resultados que se ven.']),('Rentabilidad bajo la lupa',['Saber cuánto ganás no alcanza. Hay que entender por qué.','Analizamos los números que determinan tu rentabilidad.\n\nCostos · Precios · Márgenes · Eficiencia','Más rentabilidad no es vender más: es gestionar mejor.']),('Procesos que suman, no que restan',['Procesos eficientes impulsan negocios escalables.','Revisamos y optimizamos tus procesos para eliminar lo que no agrega valor.\n\nMenos tiempos muertos · Menos errores · Más eficiencia','Equipos más productivos, clientes más satisfechos, negocios más fuertes.']),('Comercializar mejor para crecer más',['Una buena oferta necesita una buena estrategia comercial.','Fortalecemos tu gestión comercial.\n\nProceso de ventas · Segmentación · Propuesta de valor · Fidelización','Más clientes correctos, más ventas y relaciones a largo plazo.']),('Decisiones hoy, resultados mañana',['Cada decisión cuenta. Hoy construís el futuro de tu negocio.','Te damos la información y el análisis que necesitás para decidir con confianza.\n\nVisión estratégica · Análisis profundo · Recomendaciones accionables','Decidir mejor hoy es asegurar mejores resultados mañana.']),('Crecer con foco y estrategia',['No se trata de hacer más, sino de hacer lo correcto.','Definimos y ejecutamos la estrategia adecuada para tu negocio.\n\nObjetivos claros · Plan de acción · Seguimiento','Estrategia + ejecución = crecimiento real y sostenible.']),('Tu negocio tiene potencial, hagámoslo crecer',['Detectamos el potencial y lo convertimos en resultados.','Diagnóstico, análisis y recomendaciones para impulsar tu negocio.\n\nMirada externa · Metodología probada · Enfoque en resultados','El momento de crecer es ahora.\n\nConstruyamos tu próxima historia de éxito.'])]
def lines(d,t,f,m):
 r=[]
 for para in t.split('\n'):
  if not para.strip(): r.append(''); continue
  cur=''
  for w in para.split():
   q=(cur+' '+w).strip()
   if d.textbbox((0,0),q,font=f)[2]<=m: cur=q
   else: r.append(cur); cur=w
  if cur:r.append(cur)
 return r
for pi,(topic,slides) in enumerate(posts,1):
 for si,body in enumerate(slides,1):
  im=Image.new('RGB',(W,H),WHITE);d=ImageDraw.Draw(im);d.rectangle((0,0,W,230),fill=NAVY);d.polygon([(820,0),(1080,0),(1080,330),(960,270)],fill=GOLD)
  d.text((70,72),'EcomPymes',font=BR,fill=WHITE);d.text((70,125),'Impulsamos tu negocio. Potenciamos tu crecimiento.',font=S,fill=(220,220,218))
  y=310
  for l in lines(d,topic,T,900): d.text((70,y),l,font=T,fill=NAVY);y+=88
  d.rectangle((70,y+18,360,y+26),fill=GOLD);y+=80
  for l in lines(d,body,B,900):
   if l=='': y+=35
   else:d.text((70,y),l,font=B,fill=DARK);y+=60
  d.rounded_rectangle((55,H-205,W-55,H-55),radius=28,fill=NAVY);d.text((85,H-175),'Soluciones simples. Resultados reales.',font=BR,fill=WHITE);d.text((85,H-125),'ecompymes.com.ar · WhatsApp +54 9 11 3956-4280',font=S,fill=(230,214,175))
  im.save(out/f'linkedin_{pi:02d}_{si:02d}.png',optimize=True)
# generated for EcomPymes LinkedIn
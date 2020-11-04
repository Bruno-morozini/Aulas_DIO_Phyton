segundo_str = input ("Por favor, entre com o número de segundos que deseja converter:" )

total_seg = int(segundo_str)

dia = total_seg // 86400

rest_dia = total_seg % 86400

hora = rest_dia // 3600 

seg_restante = total_seg %3600

minutos = seg_restante // 60

seg_restante_final  =  seg_restante % 60



print( dia, "dias,", hora, "horas, " , minutos , "minutos  e" , seg_restante_final, "segundos.",  )




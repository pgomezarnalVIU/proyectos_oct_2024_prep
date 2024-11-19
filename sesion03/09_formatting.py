# {[argument_index_or_keyword]:[width][.precision][type]}

numero_decimal_largo = 12.3456234569254
numero_entero_largo = 45628945.676

print(f"Solo imprimimos dos decimales |{numero_decimal_largo:0.2f}|")
print(f"Solo imprimimos dos decimales |{numero_entero_largo:0.2f}|")

print(f"Solo imprimimos 5 de longitud y 2 decimales |{numero_decimal_largo:5.2f}|")
print(f"Solo imprimimos 5 de longitud y 2 decimales |{numero_entero_largo:5.2f}|")

print(f"Solo imprimimos 15 de longitud y 2 decimales |{numero_decimal_largo:15.2f}|")
print(f"Solo imprimimos 15 de longitud y 2 decimales |{numero_entero_largo:15.2f}|")

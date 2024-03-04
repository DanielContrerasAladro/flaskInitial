from ejemplo8 import basededatos, Mascota

basededatos.create_all()

mascota1 = Mascota("debra")

basededatos.session.add_all( [ mascota1 ] )
basededatos.session.commit()


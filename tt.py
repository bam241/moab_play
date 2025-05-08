import pydagmc
m = pydagmc.Model("rtttest_mcnp_mesh.rtt")
print(m.volumes_by_material)
m.write_file("out.h5")

from jnius import autoclass

fname = 'data/biopax3-short-metabolic-pathway.owl'
io_class = autoclass('org.biopax.paxtools.io.SimpleIOHandler')
io = io_class(autoclass('org.biopax.paxtools.model.BioPAXLevel').L3)
file_is = autoclass('java.io.FileInputStream')(fname)
model = io.convertFromOWL(file_is)

print('ALL ELEMENTS:')

elements = model.getObjects().toArray()
for current_element in elements:
    rdf_id = current_element.getUri()
    class_name = current_element.getClass().getName()
    print('Element: %s : %s' % (rdf_id, class_name))

print('PROTEINS ONLY:')

protein_class = autoclass('org.biopax.paxtools.model.level3.Protein')
proteins = model.getObjects(protein_class).toArray()
for current_protein in proteins:
    print('%s: %s' % (current_protein.getName().toArray(),
                      current_protein.getDisplayName()))

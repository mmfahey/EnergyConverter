compatible_units = ('eV', 'nm', 'wavenumber', 'hartree', 'kcal/mol', 'kJ/mol')

def convert2eV(energy, units):
    if units == 'eV':
        print(f'{energy} eV')
    if units == 'nm' :
        print(f'{((1/float(energy))*1240)} eV')
    if units == 'wavenumber':
        print(f'{float(energy)/8065.6} eV')
    if units == 'hartree':
        print(f'{float(energy)/3.6749E-2} eV')
    if units == 'kcal/mol':
        print(f'{float(energy)/23.061} eV')
    if units == 'kJ/mol':
        print(f'{float(energy)/96.485} eV')

def convert2nm(energy, units):
    if units == 'eV':
        print(f'{(1240/float(energy))} nm')
    if units == 'nm':
        print(f'{energy} nm')
    if units == 'wavenumber':
        print(f'{10000000/float(energy)} nm')
    if units == 'hartree':
        print(f'{1240/(float(energy)/3.6749E-2)} nm')
    if units == 'kcal/mol':
        print(f'{1240/(float(energy)/23.061)} nm')
    if units == 'kJ/mol':
        print(f'{1240/(float(energy)/96.485)} nm')

def convert2wavenumber(energy, units):
    if units == 'eV':
        print(f'{float(energy)*8065.6} wavenumber')
    if units == 'nm':
        print(f'{(1/float(energy)*10000000)} wavenumber')
    if units == 'wavenumber':
        print(f'{energy} wavenumber')
    if units == 'hartree':
        print(f'{float(energy)/4.5563E-6} wavenumber')
    if units == 'kcal/mol':
        print(f'{float(energy)/2.8591E-3} wavenumber')
    if units == 'kJ/mol':
        print(f'{float(energy)/1.1963E-2} wavenumber')

def convert2hartree(energy, units):
    if units == 'eV':
        print(f'{float(energy)/27.212} hartree')
    if units == 'nm':
        print(f'{((1/float(energy))*1240)/27.212} hartree')
    if units == 'wavenumber':
        print(f'{float(energy)/2.1947E5} hartree')
    if units == 'hartree':
        print(f'{float(energy)} hartree')
    if units == 'kcal/mol':
        print(f'{float(energy)/627.51} hartree')
    if units == 'kJ/mol':
        print(f'{float(energy)/2625.50} hartree')

def convert2kcal(energy,units):
    if units == 'eV':
        print(f'{float(energy)/4.3363E-2} kcal/mol')
    if units == 'nm':
        print(f'{((1/float(energy))*1240)/4.3363E-2} kcal/mol')
    if units == 'wavenumber':
        print(f'{float(energy)/349.75} kcal/mol')
    if units == 'hartree':
        print(f'{float(energy)/1.5936E-3} kcal/mol')
    if units == 'kcal/mol':
        print(f'{float(energy)} kcal/mol')
    if units == 'kJ/mol':
        print(f'{float(energy)/4.1840} kcal/mol')

def convert2joule(energy, units):
    if units == 'eV':
        print(f'{float(energy)/1.0364E-2} kJ/mol')
    if units == 'nm':
        print(f'{((1/float(energy))*1240)/1.0364E-2} kJ/mol')
    if units == 'wavenumber':
        print(f'{float(energy)/83.593} kJ/mol')
    if units == 'hartree':
        print(f'{float(energy)/3.8088E-4} kJ/mol')
    if units == 'kcal/mol':
        print(f'{float(energy)/0.23901} kJ/mol')
    if units == 'kJ/mol':
        print(f'{float(energy)} kJ/mol')

def main():
    print(f'Compatible units: {compatible_units}')
    units = input('Units of value you want to convert: ')
    #check that unit input is in compatible units
    if units in compatible_units:
        energy = input(f'Energy in {units} to convert: ')
    #Convert to  hartree, kcal, um, Thz, ps
        print('-'*50)
        convert2eV(energy, units)
        convert2nm(energy, units)
        convert2wavenumber(energy, units)
        convert2hartree(energy, units)
        convert2kcal(energy,units)
        convert2joule(energy,units)
        print('-'*50)
    else:
        print(f'Did not enter a compatible unit or with the correct syntax{compatible_units}')

if __name__ == '__main__':
    main()
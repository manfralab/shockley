''' helpers to load configuration without dealing with paths in notebook '''

from pathlib import Path, PurePath
import sqpurdue

yaml_lookup = {
    'BlueFors': 'BFXLD1.yaml',
    '4K magnet': 'oxford_4K_magnet_station.yaml',
}

def get_config_path(system_name):
    ''' load config path by system name '''

    if system_name in yaml_lookup:
        module_path = Path(sqpurdue.__file__).parent
        config_path = module_path / Path('station_configurations/{0:s}'.format(yaml_lookup[system_name]))
        return str(config_path)
    else:
        raise ValueError(f'{system_name} is not a recognized system name.')

def clear_station_instruments(st):
    conn_instr = [instr for instr in st.components if not instr=='config']
    for inst in conn_instr:
        try:
            st.close_and_remove_instrument(inst)
        except Exception as e:
            print(e)
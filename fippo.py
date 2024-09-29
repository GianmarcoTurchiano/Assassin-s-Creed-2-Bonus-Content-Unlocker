import os
import argparse

def set_bytes_to_1(file_path, cloud_save):
    byte_positions = [
        # Deluxe Edition bonuses:
        0x5F2, # Palazzo Medici Templar Lair
        0x604, # Santa Maria dei Frari Templar Lair
        0x616, # Arsenale di Venezia Templar Lair
        0x63A, # Bonus outfit dye
        # Ubisoft Connect rewards:
        0x694, # Throwing knives capacity upgrade
        0x6A6, # Altaïr's outfit
        0x6B8, # Auditore Family Crypt
        # Bloodlines weapons:
        0x78B, # Maria Thorpe's Longsword
        0x78C, # Fredrick's Hammer
        0x78D, # Mace of the Bull
        0x78E, # Dark Oracle's Bone Dagger
        0x78F, # Twins' Rapier
        0x790, # Bouchart's Blade
    ]

    with open(file_path, 'rb') as file:
        binary_data = bytearray(file.read())

        for position in byte_positions:
            binary_data[position] = 0x01

    if cloud_save:
        cloud_file_path = f'{file_path}.upload'

        with open(cloud_file_path, 'wb') as file:
            file.write(binary_data)

        print(f'The modified file has been saved as "{cloud_file_path}".')
    else:
        with open(file_path, 'wb') as file:
            file.write(binary_data)
    
        print(f'The modified file is "{file_path}".')

def find_smaller_file(root):
    filepath_1 = f'{root}/1.save'
    filepath_2 = f'{root}/2.save'
    
    if not os.path.exists(filepath_1):
        raise Exception(f"No {filepath_1} found.")
        
    if not os.path.exists(filepath_2):
        raise Exception(f"No {filepath_2} found.")
 
    size1 = os.path.getsize(filepath_1)
    size2 = os.path.getsize(filepath_2)
    
    return filepath_1 if size1 < size2 else filepath_2
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update specific bytes in a save file.')
    parser.add_argument('file_path', type=str, help='Path to the save file.')
    parser.add_argument('--cloud-save', action='store_true', help='Save the modified file with ".upload" suffix.')

    try:
        args = parser.parse_args()
    
        file_path = find_smaller_file(args.file_path)
        set_bytes_to_1(file_path, args.cloud_save)
    except Exception as e:
        print(f'ERROR: {e}')
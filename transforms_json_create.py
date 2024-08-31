import os
import json
import numpy as np

def generate_transforms_json(base_path):
    instance_paths = [os.path.join(base_path, d) for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    for instance_path in instance_paths:
        cameras_file = os.path.join(instance_path, 'cameras.npz')
        if not os.path.exists(cameras_file):
            print(f"Warning: cameras.npz not found in {instance_path}")
            continue

        try:
            cameras_data = np.load(cameras_file)
            print(f"Loaded cameras.npz for {instance_path}")
        except Exception as e:
            print(f"Error loading cameras.npz in {instance_path}: {e}")
            continue

        frames = []

        # Find all world_mat and intrinsic_mat keys
        world_mats = [key for key in cameras_data if key.startswith('world_mat_')]
        intrinsic_mats = [key for key in cameras_data if key.startswith('camera_mat_')]

        for i, world_mat_key in enumerate(world_mats):
            frame = {
                "file_path": os.path.join('image', f'{i:04d}.png').replace("\\", "/"),
                "transform_matrix": cameras_data[world_mat_key].tolist()
            }
            frames.append(frame)

        if intrinsic_mats:
            try:
                # Assuming the intrinsic matrix is the same for all images
                sample_intrinsic = cameras_data[intrinsic_mats[0]]
                print(f"Sample intrinsic matrix: {sample_intrinsic}")
                focal_length = sample_intrinsic[0, 0]
                camera_angle_x = float(2 * np.arctan(1.0 / focal_length))
            except Exception as e:
                print(f"Error calculating camera_angle_x: {e}")
                camera_angle_x = np.pi / 4  # Default value
                print(f"Using default camera_angle_x: {camera_angle_x}")
        else:
            camera_angle_x = np.pi / 4  # Default value
            print(f"Warning: intrinsic_mats not found in {instance_path}, using default camera_angle_x.")

        transforms = {
            "camera_angle_x": camera_angle_x,
            "frames": frames
        }

        transforms_file = os.path.join(instance_path, 'transforms.json')
        try:
            with open(transforms_file, 'w') as f:
                json.dump(transforms, f, indent=4)
            print(f"Generated transforms.json for {instance_path}")
        except Exception as e:
            print(f"Error writing transforms.json in {instance_path}: {e}")

if __name__ == "__main__":
    base_path = 'src/data/NMR_Dataset/000'  # Adjust this path to your dataset location
    generate_transforms_json(base_path)

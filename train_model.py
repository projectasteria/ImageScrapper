import yaml,json, logging, os, shutil, multiprocessing

def run_job(command):
    os.system(command)

def train_model(model_definition, output_dir, data_csv, experiment_name, log_file):
    
    command = "ludwig train --data_csv {} --output_directory {} --experiment_name {} --model_definition_file {} > {}".format(data_csv, output_dir, experiment_name, model_definition, log_file)

    print (command)
    run_job(command)
    # p = multiprocessing.Process(target=run_job, args=(command,))
    # p.start()
    return True


# model_definition = "mnist_png/model_definition.yaml"
# data_csv = "mnist_png/mnist_dataset_training.csv"
# experiment_name = "test_exp"

# train_model(model_definition, data_csv, experiment_name)

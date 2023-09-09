import configparser
import pandas as pd

def extract_patients_info_to_csv(train=True):
    """
    Extract patients info from info.cfg files and export to csv
    :param train: True if train, False if test
    :return: patients info dataframe
    """
    patient_cfg = configparser.ConfigParser()

    data = pd.DataFrame(columns=['patient_id', 'group', 'bmi_category', 'bmi', 'height', 'weight', 'nb_frame', 'ed', 'es'])

    if train:
        path = './data/training/patient'
        patients_range = range(1, 101)
    else:
        path = './data/testing/patient'
        patients_range = range(101, 151)    

    for i in patients_range:
        idx = str(i).zfill(3)
        patient_cfg.read_string('[Info]\n' + open(path + idx + '/info.cfg').read())

        ed = patient_cfg.get('Info', 'ED')
        es = patient_cfg.get('Info', 'ES')
        group = patient_cfg.get('Info', 'Group')
        nb_frame = patient_cfg.get('Info', 'NbFrame')
        height = float(patient_cfg.get('Info', 'Height'))
        weight = float(patient_cfg.get('Info', 'Weight'))
        bmi = weight / (height / 100) ** 2
        bmi_category = 'Healthy'
        """
        If your BMI is less than 18.5, it falls within the underweight range.
        If your BMI is 18.5 to <25, it falls within the healthy weight range.
        If your BMI is 25.0 to <30, it falls within the overweight range.
        If your BMI is 30.0 or higher, it falls within the obesity range.
        """
        if bmi < 18.5:
            bmi_category = 'Underweight'
        elif bmi < 25:
            bmi_category = 'Healthy'
        elif bmi < 30:
            bmi_category = 'Overweight'
        else:
            bmi_category = 'Obesity'

        data.loc[i] = [idx, group, bmi_category, bmi, height, weight, nb_frame, ed, es]

    # export to csv
    if train:
        export_path = './info/train_patients_info.csv'
    else:
        export_path = './info/test_patients_info.csv'
    data.to_csv(export_path, index=False)

    return data
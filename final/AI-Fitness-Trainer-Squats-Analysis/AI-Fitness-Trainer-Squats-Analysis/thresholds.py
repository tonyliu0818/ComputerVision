
# 判斷狀態的角度
# Get thresholds for beginner mode
def get_thresholds_beginner():

    _ANGLE_HIP_KNEE_VERT = {
        # s1
        'NORMAL': (0,  32),
        # s2
        # 'TRANS'  : (35, 65),
        # s3
        'PASS': (35, 95)
    }

    thresholds = {
        'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

        'HIP_THRESH': [10, 50],
        'ANKLE_THRESH': 45,
        'KNEE_THRESH': [50, 65, 100],

        'OFFSET_THRESH': 35.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50

    }

    return thresholds


# Get thresholds for pro mode
def get_thresholds_pro():

    _ANGLE_HIP_KNEE_VERT = {
        'NORMAL': (0,  32),
        'TRANS': (35, 65),
        'PASS': (85, 90)
    }

    thresholds = {
        'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

        'HIP_THRESH': [15, 50],
        'ANKLE_THRESH': 30,
        'KNEE_THRESH': [50, 85, 90],

        'OFFSET_THRESH': 35.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50

    }

    return thresholds


def get_thresholds_normal():

    _ANGLE_HIP_KNEE_VERT = {
        # s1
        'NORMAL': (0,  32),
        # s2
        'TRANS': (35, 65),
        # s3
        'PASS': (70, 95)
    }

    thresholds = {
        'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

        'HIP_THRESH': [10, 50],
        'ANKLE_THRESH': 40,
        'KNEE_THRESH': [50, 70, 95],

        'OFFSET_THRESH': 35.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50

    }

    return thresholds

import pandas as pd
import numpy as np
score_array = np.random.randint(50,high = 101, size=(50,5))
# score_array 沒有索引欄位
student_dataFrame = pd.DataFrame(data = score_array,
             index= range(1,51),
             columns=['國文','英文','數學','自然','社會'])
student_dataFrame
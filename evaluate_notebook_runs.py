import unittest
import xmlrunner
import json
import glob
import os

class TestJobOutput(unittest.TestCase):

  test_output_path = f"/Workspace${os.getenv('WORKSPACEBUNDLEPATH')}/Validation/Output"

  def test_performance(self):
    path = self.test_output_path
    statuses = []

    for filename in glob.glob(os.path.join(path, '*.json')):
      print('Evaluating: ' + filename)

      with open(filename) as f:
        data = json.load(f)

        duration = data['tasks'][0]['execution_duration']

        if duration > 100000:
            status = 'FAILED'
        else:
            status = 'SUCCESS'

        statuses.append(status)
        f.close()

    self.assertFalse('FAILED' in statuses)

  def test_job_run(self):
    path = self.test_output_path
    statuses = []

    for filename in glob.glob(os.path.join(path, '*.json')):
      print('Evaluating: ' + filename)

      with open(filename) as f:
        data = json.load(f)
        status = data['state']['result_state']
        statuses.append(status)
        f.close()

    self.assertFalse('FAILED' in statuses)

if __name__ == '__main__':
  unittest.main(
    testRunner = xmlrunner.XMLTestRunner(
      output = f"/Workspace${os.getenv('WORKSPACEBUNDLEPATH')}/Validation/Output/test-results",
    ),
    failfast   = False,
    buffer     = False,
    catchbreak = False,
    exit       = False
  )

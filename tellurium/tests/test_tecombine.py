"""
Testing tecombine.
"""
# TODO: implement additional tests/real tests of content.

from __future__ import print_function

import os
import shutil
import tempfile
import unittest

import tellurium as te


class tecombineTestCase(unittest.TestCase):
    """ Testcases for tecombine. """

    def setUp(self):
        # create a test instance
        self.antimony = '''
        model myModel
          S1 -> S2; k1*S1
          S1 = 10; S2 = 0
          k1 = 1
        end
        '''
        self.newAntimony = '''
        model newAntimony
          S1 -> S2; k1*S1
          S1 = 10; S2 = 0
          k1 = 1
        end
        '''
        self.phrasedml = '''
          model1 = model "myModel"
          sim1 = simulate uniform(0, 5, 100)
          task1 = run sim1 on model1
          plot "Figure 1" time vs S1, S2
        '''
        self.newPhrasedml = '''
          model1 = model "newAntimony"
          sim1 = simulate uniform(0, 10, 100)
          task1 = run sim1 on model1
          plot "Figure 1" time vs S1, S2
        '''
        exp = te.experiment(self.antimony, self.phrasedml)

        self.tmpdir = tempfile.mkdtemp()
        self.tmparchive = os.path.join(self.tmpdir, 'test.zip')

        exp.exportAsCombine(self.tmparchive)
        self.com = te.combine(self.tmparchive)
        
    def test_addantimony(self):
        """ Test addAntimony. """
        self.com.addAntimony(self.newAntimony)
        self.clearTest()
    
    def test_addphrasedml(self):
        """ Test addPhrasedml. """
        self.com.addPhrasedml(self.newPhrasedml, self.newAntimony, 
                              arcname="newphrasedml.xml")
        self.clearTest()
        
    def test_getsbml(self):
        """ Test getSBML. """
        sbmlstr = self.com.getSBML("myModel.xml")
        self.assertIsNotNone(sbmlstr)
        self.clearTest()
    
    def test_getsbmlasantimony(self):
        """ Test getSBMLAsAntimony. """
        antstr = self.com.getSBMLAsAntimony("myModel.xml")
        self.assertIsNotNone(antstr)
        self.clearTest()
    
    def test_getsedml(self):
        """ Test getSEDML."""
        sedmlstr = self.com.getSEDML("experiment1.xml")
        self.assertIsNotNone(sedmlstr)
        self.clearTest()
    
    def test_getsedmlaspharsedml(self):
        """ Test getSEDMLAsPhrasedml. """
        phrasedmlstr = self.com.getSEDMLAsPhrasedml("experiment1.xml")
        self.assertIsNotNone(phrasedmlstr)
        self.clearTest()
    
    def test_listcontents(self):
        """ Test listContents. """
        contents = self.com.listContents()
        self.assertIsNotNone(contents)
        self.clearTest()
        
    def test_listdetailedcontents(self):
        """ Test listDetailedContents. """
        detailedContents = self.com.listDetailedContents()
        print(detailedContents)
        self.assertIsNotNone(detailedContents)
        self.clearTest()
    
    def test_readmanifest(self):
        """ Test readManifest. """
        man = self.com.readManifest()
        self.assertIsNotNone(man)
        self.clearTest()
    
    def clearTest(self):
        shutil.rmtree(self.tmpdir)

    def writingAndReadingExecution(self):
        antimonyStr = '''
        model myModel
          S1 -> S2; k1*S1;
          S1 = 10; S2 = 0;
          k1 = 1;
        end
        '''
        phrasedmlStr = '''
          model1 = model "myModel"
          sim1 = simulate uniform(0, 5, 100)
          task1 = run sim1 on model1
          plot "Figure 1" time vs S1, S2
          report time vs S1, S2
        '''
        import tellurium as te

        # Create experiment
        exp = te.experiment(antimonyStr, phrasedmlStr)
        # Run and store with results
        tmpdir = tempfile.mkdtemp()
        exp.exportAsCombineWithOutputs(os.path.join(tmpdir, 'test.omex'))
        # Execute the created archive
        te.executeOMEX('test.omex', workingDir=tmpdir)
        shutil.rmtree(tmpdir)

    
if __name__ == '__main__':
    unittest.main()    

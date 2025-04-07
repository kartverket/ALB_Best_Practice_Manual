"""
Model exported as python.
Name : ALB_QC_v2
Group : 
With QGIS : 33600
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterPointCloudLayer
from qgis.core import QgsProcessingParameterVectorDestination
from qgis.core import QgsProcessingParameterRasterDestination
import processing


class Alb_qc_v2(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterPointCloudLayer('alb_copc_pointcloudvpc', 'alb_copc_pointcloud.vpc', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorDestination('Qcwaterdepth_1mshp', '/QC/waterdepth_1m.shp', type=QgsProcessing.TypeVectorLine, createByDefault=True, defaultValue='C:/Users/malchr/AppData/Roaming/QGIS/QGIS3/profiles/default/processing/outputs/waterdepth_1m.shp'))
        self.addParameter(QgsProcessingParameterRasterDestination('Qcwaterdepth_1mtif', '/QC/waterdepth_1m.tif', createByDefault=True, defaultValue='C:/Users/malchr/AppData/Roaming/QGIS/QGIS3/profiles/default/processing/outputs/waterdepth_1m.tif'))
        self.addParameter(QgsProcessingParameterRasterDestination('Topobathy_2m_density_ok_at_2mtif', 'topobathy_2m_density_OK_at_2m.tif', createByDefault=True, defaultValue=''))
        self.addParameter(QgsProcessingParameterRasterDestination('Qctopobathy_2m_densitytif', '/QC/topobathy_2m_density.tif', createByDefault=True, defaultValue='C:/Users/malchr/AppData/Roaming/QGIS/QGIS3/profiles/default/processing/outputs/topobathy_2m_density.tif'))
        self.addParameter(QgsProcessingParameterRasterDestination('Qctopobathy_1m_dtmtif', '/QC/topobathy_1m_dtm.tif', createByDefault=True, defaultValue='C:/Users/malchr/AppData/Roaming/QGIS/QGIS3/profiles/default/processing/outputs/topobathy_1m_dtm.tif'))
        self.addParameter(QgsProcessingParameterRasterDestination('Qctopobathy_1m_watersurfacetif', '/QC/topobathy_1m_watersurface.tif', createByDefault=True, defaultValue='C:/Users/malchr/AppData/Roaming/QGIS/QGIS3/profiles/default/processing/outputs/topobathy_1m_watersurface.tif'))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(9, model_feedback)
        results = {}
        outputs = {}

        # ### 7. Calculate Density
        alg_params = {
            'FILTER_EXPRESSION': 'Classification = 2 OR Classification = 40',
            'FILTER_EXTENT': None,
            'INPUT': parameters['alb_copc_pointcloudvpc'],
            'ORIGIN_X': None,
            'ORIGIN_Y': None,
            'RESOLUTION': 2,
            'TILE_SIZE': 1000,
            'OUTPUT': parameters['Qctopobathy_2m_densitytif']
        }
        outputs['7CalculateDensity'] = processing.run('pdal:density', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Qctopobathy_2m_densitytif'] = outputs['7CalculateDensity']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # ### 4. Build Watersurface
        alg_params = {
            'FILTER_EXPRESSION': 'Classification = 2 OR Classification = 41',
            'FILTER_EXTENT': None,
            'INPUT': parameters['alb_copc_pointcloudvpc'],
            'ORIGIN_X': None,
            'ORIGIN_Y': None,
            'RESOLUTION': 1,
            'TILE_SIZE': 1000,
            'OUTPUT': parameters['Qctopobathy_1m_watersurfacetif']
        }
        outputs['4BuildWatersurface'] = processing.run('pdal:exportrastertin', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Qctopobathy_1m_watersurfacetif'] = outputs['4BuildWatersurface']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # ### 3. Build Topobaty DTM
        alg_params = {
            'ATTRIBUTE': 'Z',
            'FILTER_EXPRESSION': 'Classification = 2 OR Classification = 40',
            'FILTER_EXTENT': None,
            'INPUT': parameters['alb_copc_pointcloudvpc'],
            'ORIGIN_X': None,
            'ORIGIN_Y': None,
            'RESOLUTION': 1,
            'TILE_SIZE': 1000,
            'OUTPUT': parameters['Qctopobathy_1m_dtmtif']
        }
        outputs['3BuildTopobatyDtm'] = processing.run('pdal:exportraster', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Qctopobathy_1m_dtmtif'] = outputs['3BuildTopobatyDtm']['OUTPUT']

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # ### 8. Calculate Density Binary Plot / Select Density > 20
        alg_params = {
            'CELL_SIZE': None,
            'CRS': parameters['alb_copc_pointcloudvpc'],
            'EXPRESSION': '"A@1" >= 20',
            'EXTENT': None,
            'LAYERS': outputs['7CalculateDensity']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['8CalculateDensityBinaryPlotSelectDensity20'] = processing.run('native:modelerrastercalc', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # ### 5. Calculate Water Depth
        alg_params = {
            'BAND_A': 1,
            'BAND_B': 1,
            'BAND_C': None,
            'BAND_D': None,
            'BAND_E': None,
            'BAND_F': None,
            'EXTENT_OPT': 2,  # Union
            'EXTRA': None,
            'FORMULA': 'B-A',
            'INPUT_A': outputs['3BuildTopobatyDtm']['OUTPUT'],
            'INPUT_B': outputs['4BuildWatersurface']['OUTPUT'],
            'INPUT_C': None,
            'INPUT_D': None,
            'INPUT_E': None,
            'INPUT_F': None,
            'NO_DATA': None,
            'OPTIONS': None,
            'PROJWIN': None,
            'RTYPE': 5,  # Float32
            'OUTPUT': parameters['Qcwaterdepth_1mtif']
        }
        outputs['5CalculateWaterDepth'] = processing.run('gdal:rastercalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Qcwaterdepth_1mtif'] = outputs['5CalculateWaterDepth']['OUTPUT']

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # ### 8. Calculate Density Binary Plot / Resample WD to 2m
        alg_params = {
            'CELL_SIZE_X': None,
            'CELL_SIZE_Y': None,
            'CRS': None,
            'EXTENT': None,
            'GRID_OFFSET_X': None,
            'GRID_OFFSET_Y': None,
            'INPUT': outputs['5CalculateWaterDepth']['OUTPUT'],
            'REFERENCE_LAYER': outputs['7CalculateDensity']['OUTPUT'],
            'RESAMPLING_METHOD': 0,  # Nearest Neighbour
            'RESCALE': False,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['8CalculateDensityBinaryPlotResampleWdTo2m'] = processing.run('native:alignsingleraster', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # ### 8. Calculate Density Binary Plot / Select 1.5 < WD < 2.5
        alg_params = {
            'CELL_SIZE': None,
            'CRS': parameters['alb_copc_pointcloudvpc'],
            'EXPRESSION': ' if ( "A@1" >= 0.5 AND "A@1" <= 2.5,1,0)',
            'EXTENT': None,
            'LAYERS': outputs['8CalculateDensityBinaryPlotResampleWdTo2m']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['8CalculateDensityBinaryPlotSelect15Wd25'] = processing.run('native:modelerrastercalc', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # ### 6. Generate Depth Contours
        alg_params = {
            'BAND': 1,
            'CREATE_3D': False,
            'EXTRA': None,
            'FIELD_NAME': 'ELEV',
            'IGNORE_NODATA': False,
            'INPUT': outputs['5CalculateWaterDepth']['OUTPUT'],
            'INTERVAL': 1,
            'NODATA': None,
            'OFFSET': 0,
            'OUTPUT': parameters['Qcwaterdepth_1mshp']
        }
        outputs['6GenerateDepthContours'] = processing.run('gdal:contour', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Qcwaterdepth_1mshp'] = outputs['6GenerateDepthContours']['OUTPUT']

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # Selection WD AND Selection Density
        alg_params = {
            'DATA_TYPE': 5,  # Float32
            'INPUT': [outputs['8CalculateDensityBinaryPlotSelect15Wd25']['OUTPUT'],outputs['8CalculateDensityBinaryPlotSelectDensity20']['OUTPUT']],
            'NODATA_AS_FALSE': False,
            'NO_DATA': -9999,
            'REF_LAYER': outputs['8CalculateDensityBinaryPlotSelect15Wd25']['OUTPUT'],
            'OUTPUT': parameters['Topobathy_2m_density_ok_at_2mtif']
        }
        outputs['SelectionWdAndSelectionDensity'] = processing.run('native:rasterbooleanand', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Topobathy_2m_density_ok_at_2mtif'] = outputs['SelectionWdAndSelectionDensity']['OUTPUT']
        return results

    def name(self):
        return 'ALB_QC_v2'

    def displayName(self):
        return 'ALB_QC_v2'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Alb_qc_v2()

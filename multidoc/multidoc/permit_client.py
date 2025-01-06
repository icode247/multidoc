from permit import Permit
import os

permit = Permit(
    pdp=os.getenv('PERMIT_PDP_URL', 'https://cloudpdp.api.permit.io'),
    token=os.getenv('PERMIT_API_KEY', "permit_key_jfXbnPOIgFTl6fQHTTghAOUjRAlPw4qdeB4tr73FP7NiIukoxmsbe9wshrgiD3EWUcT8pupZpbyy3JhnjpDkdw")
)
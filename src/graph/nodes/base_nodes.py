from src.llm.invoke import  generate_section
from src.graph.state import GraphState
from src.llm.invoke import generate_functional_requirements_group



class BaseNodes:
    
    def __init__(self) -> None:
        pass
    

    
    async def proposed_system_node(self,state:GraphState,prompt_template, output_model,run_name):

 
        interfaces_and_users = state.get("interfaces_and_users")
        modules_and_features= state.get('functional_requirements_plan')

        prompt_variables = {"interfaces_and_users":interfaces_and_users, "modules_and_features":modules_and_features}
            
        response= await generate_section(
            state=state,
            prompt_template=prompt_template,
            output_model= output_model,
            run_name= run_name,
            prompt_variables=prompt_variables

        )
        return response
    
    async def timeline_node(self,state:GraphState,prompt_template, output_model,run_name,is_timeline):
            
        response= await generate_section(
            state=state,
            prompt_template=prompt_template,
            output_model= output_model,
            run_name= run_name,
            is_timeline=is_timeline

        )
        
        return response
    
    async def functional_requirements_node(self,state:GraphState,prompt_template, output_model,run_name):
        context = state["context"]
        project_title = context['project_name']
        project_understanding = state.get("enhanced_context")
        interfaces_and_users = state.get('interfaces_and_users')
        functional_requirements_plan = state.get('functional_requirements_plan')
        prompt_variables = {"project_title":project_title, "project_understanding":project_understanding,
                             "interfaces_and_users":interfaces_and_users, 'functional_requirements_plan':functional_requirements_plan}

        response= await generate_section(
            state=state,
            prompt_template=prompt_template,
            output_model= output_model,
            run_name= run_name,
            prompt_variables=prompt_variables

        )
        return response
    
    # async def functional_requirements_operations_node(self,state:GraphState, enhanced_context,output_model,
    #     group_plan,run_name,prompt_template):

        
    #     response= await generate_functional_requirements_group(
    #         enhanced_context=enhanced_context,
    #         group_plan=group_plan,
    #         run_name=run_name,
    #         output_model=output_model,
    #         prompt_template=prompt_template
    #     )
        
    #     return response



    # async def  functional_requirements_internal_management_node(self,state:GraphState,enhanced_context,prompt_template,output_model,group_plan,run_name):

        
    #     response= await generate_functional_requirements_group(
    #         enhanced_context=enhanced_context,
    #         group_plan=group_plan,
    #         run_name=run_name,
    #         output_model=output_model,
    #         prompt_template=prompt_template
    #     )

    #     return response

    # async def functional_requirements_client_experience_node(self,state:GraphState,enhanced_context,prompt_template,output_model,group_plan,run_name) :
    

    #     response = await generate_functional_requirements_group(
    #             enhanced_context= enhanced_context,
    #             group_plan= group_plan,
    #             run_name= run_name,
    #             output_model=output_model,
    #             prompt_template=prompt_template
    #         )
        

    #     return response


    # async def functional_requirements_merge_node(self,state:GraphState,validate_model,output_model,keys) :

    #     keys=keys

    #     groups=[]

    #     for key in keys:
    #         group=state.get(key)
    #         if group:
    #             groups.append(validate_model(**state[key]))

    #     result = output_model(content=groups)

    #     return result


    async def Final_BRD_node(self,state,output_schema,keys):

        sections=[]

        for key in keys:
            v=state.get(key)
            if v :
                sections.append(v)
        result = output_schema(sections=sections)

        return result
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators



@CrewBase
class InternalProfileUpdate():
    """InternalProfileUpdate crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def sections_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['sections_reviewer'], # type: ignore[index]
            llm="gpt-5",
            verbose=True,
            allow_delegation=False
        )

    """
    @agent
    def json_assembler(self) -> Agent:
        return Agent(
            config=self.agents_config['json_assembler'], # type: ignore[index]
            llm="gpt-5",
            verbose=True,
            allow_delegation=False
        )
    """


    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    

    @task
    def reviewing_section_client_overview_and_status_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_client_overview_and_status_task'], # type: ignore[index]
            output_file='outputs/01.client_overview_and_status.json'
        )
    
    @task
    def reviewing_section_search_parameters_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_search_parameters_task'], # type: ignore[index]
            output_file='outputs/02.search_parameters.json'
        )
    
    
    @task
    def reviewing_section_financial_profile_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_financial_profile_task'], # type: ignore[index]
            output_file='outputs/03.financial_profile.json'
        )
    
    @task
    def reviewing_section_business_characteristics_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_business_characteristics_task'], # type: ignore[index]
            output_file='outputs/04.business_characteristics.json'
        )

    @task
    def reviewing_section_professional_background_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_professional_background_task'], # type: ignore[index]
            output_file='outputs/05.professional_background.json'
        )

    @task
    def reviewing_section_development_areas_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_development_areas_task'], # type: ignore[index]
            output_file='outputs/06.development_areas.json'
        )

    @task
    def reviewing_section_work_environment_fit_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_work_environment_fit_task'], # type: ignore[index]
            output_file='outputs/07.work_environment_fit.json'
        )

    @task
    def reviewing_section_deal_experience_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_deal_experience_task'], # type: ignore[index]
            output_file='outputs/08.deal_experience.json'
        )

    @task
    def reviewing_section_personal_and_family_context_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_personal_and_family_context_task'], # type: ignore[index]
            output_file='outputs/09.personal_and_family_context.json'
        )

    @task
    def reviewing_section_interests_and_influences_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_interests_and_influences_task'], # type: ignore[index]
            output_file='outputs/10.interests_and_influences.json'
        )

    @task
    def reviewing_section_psychology_and_coaching_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_psychology_and_coaching_insights_task'], # type: ignore[index]
            output_file='outputs/11.psychology_and_coaching_insights.json'
        )

    @task
    def reviewing_section_behavioral_snapshot_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_behavioral_snapshot_task'], # type: ignore[index]
            output_file='outputs/11a.behavioral_snapshot.json'
        )

    @task
    def reviewing_section_business_fit_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_business_fit_evaluation_task'], # type: ignore[index]
            output_file='outputs/12.business_fit_evaluation.json'
        )

    @task
    def reviewing_section_interaction_notes_and_red_flags_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_interaction_notes_and_red_flags_task'], # type: ignore[index]
            output_file='outputs/13.interaction_notes_and_red_flags.json'
        )

    @task
    def reviewing_section_at_a_glance_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_at_a_glance_task'], # type: ignore[index]
            output_file='outputs/14.at_a_glance.json'
        )

    @task
    def reviewing_section_client_stated_excitement_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_client_stated_excitement_task'], # type: ignore[index]
            output_file='outputs/15.client_stated_excitement.json'
        )

    @task
    def reviewing_section_recommended_business_types_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_recommended_business_types_task'], # type: ignore[index]
            output_file='outputs/16.recommended_business_types.json'
        )

    @task
    def reviewing_section_analyst_ai_fit_recommendations_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_analyst_ai_fit_recommendations_task'], # type: ignore[index]
            output_file='outputs/17.analyst_ai_fit_recommendations.json'
        )

    @task
    def reviewing_section_low_fit_or_misfit_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_low_fit_or_misfit_task'], # type: ignore[index]
            output_file='outputs/18.low_fit_or_misfit.json'
        )

    #@task
    #def reviewing_section_avoid_categories_task(self) -> Task:
    #    return Task(
    #        config=self.tasks_config['reviewing_section_avoid_categories_task'], # type: ignore[index]
    #        output_file='outputs/19.avoid_categories.json'
    #    )

    @task
    def reviewing_section_outreach_tracker_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_outreach_tracker_task'], # type: ignore[index]
            output_file='outputs/20.outreach_tracker.json'
        )



    @task
    def reviewing_section_evolution_tracking_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_evolution_tracking_task'], # type: ignore[index]
            output_file='outputs/21.evolution_tracking.json'
        )

    @task
    def reviewing_section_psychology_signals_since_last_update_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_section_psychology_signals_since_last_update_task'], # type: ignore[index]
            output_file='outputs/22.psychology_signals_since_last_update.json'
        )

    """
    @task
    def assembling_sections_task(self) -> Task:
        return Task(
            config=self.tasks_config['assembling_sections_task'], # type: ignore[index]
            output_file='outputs/23.internal_profile.json'
        )
    """
    

    @crew
    def crew(self) -> Crew:
        """Creates the InternalProfileUpdate crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

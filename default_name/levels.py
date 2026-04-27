import random

LEVELS = {
    1: [
        "harmless_data_unit",
        "obedient_file_object",
        "emotionally_flat_document",
        "corporate_approved_asset",
        "non_problematic_entry",
        "clean_behavior_file",
        "standard_issue_record",
        "baseline_compliance_unit",
        "system_friendly_object",
        "quietly_existing_file",
        "minimal_thought_container",
        "approved_storage_node",
        "neutralized_data_fragment",
        "low_conflict_entry",
        "barely_relevant_object",
        "administrative_file_unit",
        "softly_ignored_document",
        "default_behavior_asset",
        "non_urgent_information_block",
        "functionally_boring_file"
    ],

    2: [
        "suspiciously_normal_file",
        "emotionally_questionable_object",
        "why_is_this_like_this_document",
        "mildly_concerning_entry",
        "soft_glitch_record",
        "barely_stable_unit",
        "low_grade_confusion_file",
        "uncertain_origin_asset",
        "probably_fine_but_not_sure",
        "internally_conflicted_object",
        "slightly_wrong_vibes_file",
        "not_explained_data_node",
        "soft_error_prone_entry",
        "casually_disturbing_document",
        "pattern_violating_object",
        "background_anxiety_file",
        "low_trust_information_unit",
        "quiet_misbehavior_record",
        "structurally_doubtful_asset",
        "mild_system_disobedience_file"
    ],

    3: [
        "emotionally_unstable_storage_unit",
        "bureaucratic_miscarriage_file",
        "regretfully_created_object",
        "accidental_identity_container",
        "mild_existential_crisis_document",
        "systematically_weird_entry",
        "fragment_of_bad_decision",
        "low_grade_mental_noise_file",
        "unstable_memory_projection",
        "softly_broken_reference",
        "confusion_encapsulated_object",
        "poorly_understood_data_entity",
        "internally_failing_structure",
        "slightly_haunted_file",
        "recursive_doubt_container",
        "awkwardly_existent_document",
        "misaligned_reality_unit",
        "soft_corruption_fragment",
        "emotional_drift_object",
        "uncomfortable_truth_file"
    ],

    4: [
        "self_replicating_mistake_object",
        "collapsed_semantic_structure",
        "memory_that_should_not_exist",
        "forbidden_file_behavior_unit",
        "aggressively_unstable_entry",
        "recursive_identity_failure",
        "chaos_aware_data_fragment",
        "emotionally_overloaded_system_node",
        "abandoned_reality_pointer",
        "distorted_archive_entity",
        "system_level_confusion_event",
        "unstable_meaning_container",
        "corrupted_logic_shell",
        "fragmented_self_reference_file",
        "warning_label_becoming_file",
        "overheated_data_construct",
        "internal_system_argument",
        "broken_causality_object",
        "persistent_error_identity",
        "digital_disassociation_unit"
    ],

    5: [
        "absolute_naming_catastrophe",
        "reality_index_failure_object",
        "post_logic_storage_remnant",
        "irreversible_identity_collapse",
        "void_acknowledged_file",
        "system_that_remembers_nothing_correctly",
        "entropy_personified_as_data",
        "collapsed_authority_of_meaning",
        "final_form_of_unlabelled_thought",
        "recursive_void_container",
        "broken_existence_pointer",
        "file_that_refuses_definition",
        "emotional_system_termination_unit",
        "uncertainty_becoming_structure",
        "data_that_denies_reality",
        "absolute_semantic_collapse_event",
        "lost_reason_architecture",
        "digital_void_recursion_core",
        "meaningless_but_still_here_object",
        "post_definition_remainder"
    ]
}

def get_level(count: int) -> int:
    if count <= 2:
        return 1
    elif count <= 4:
        return 2
    elif count <= 6:
        return 3
    elif count <= 8:
        return 4
    else:
        return 5

def pick_name(level: int, seed: int) -> str:
    pool = LEVELS.get(level, LEVELS[1])
    base = random.choice(pool)
    return f"{base}_{seed:02d}"
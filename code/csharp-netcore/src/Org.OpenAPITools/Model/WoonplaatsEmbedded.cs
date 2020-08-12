/* 
 * Huidige bevragingen API
 *
 * Deze API levert actuele gegevens over adressen, adresseerbaar objecten en panden. Actueel betekent in deze API `zonder eindstatus`. De bron voor deze API is de basisregistratie adressen en gebouwen (BAG).
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: bag@kadaster.nl
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// WoonplaatsEmbedded
    /// </summary>
    [DataContract]
    public partial class WoonplaatsEmbedded :  IEquatable<WoonplaatsEmbedded>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="WoonplaatsEmbedded" /> class.
        /// </summary>
        /// <param name="geometrie">geometrie.</param>
        public WoonplaatsEmbedded(VlakOfMultivlak geometrie = default(VlakOfMultivlak))
        {
            this.Geometrie = geometrie;
        }
        
        /// <summary>
        /// Gets or Sets Geometrie
        /// </summary>
        [DataMember(Name="geometrie", EmitDefaultValue=false)]
        public VlakOfMultivlak Geometrie { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class WoonplaatsEmbedded {\n");
            sb.Append("  Geometrie: ").Append(Geometrie).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as WoonplaatsEmbedded);
        }

        /// <summary>
        /// Returns true if WoonplaatsEmbedded instances are equal
        /// </summary>
        /// <param name="input">Instance of WoonplaatsEmbedded to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(WoonplaatsEmbedded input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Geometrie == input.Geometrie ||
                    (this.Geometrie != null &&
                    this.Geometrie.Equals(input.Geometrie))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Geometrie != null)
                    hashCode = hashCode * 59 + this.Geometrie.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
